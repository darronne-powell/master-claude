#!/usr/bin/env python3
"""Job-open spacing for one Upwork account.

Upwork refuses job-detail opens (find_jobs action=get) when an account opens
too many too fast, and the block hits every session on that login. Every open,
from the routine or from chat, goes through this one counter.

Rules:
  - Opens are spaced at least 30 seconds apart, one at a time, from any session
    (the script waits for you).
  - One job refused: that job is skipped for good.
  - Two different jobs refused in a row: every open stops until the next
    00:00 UTC. After the pause only one test open is allowed; if it is refused,
    the pause runs to the following 00:00 UTC.

Commands:
  run-start                         routine only: go / no-go for this run
  open <job_id> [--source routine|chat]
                                    right BEFORE each find_jobs get; exit 0 = open it
  result <job_id> ok|refused        right AFTER each find_jobs get
  status                            what the counter knows
  pause [--until ISO]               stop all opens (default: next 00:00 UTC)
  unpause                           lift a pause (owner's word only)

Exit codes for `open`: 0 ok, 2 paused, 3 job skipped for good, 6 test open
already in flight. Standard library only. OPEN_BUDGET_FILE overrides the state
file path.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import fcntl  # macOS and Linux; on Windows runs are unlocked, which is fine for one routine
except ImportError:
    fcntl = None

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILE = ROOT / "state" / "open-budget.json"
SPACING_SECONDS = 30
KEEP_DAYS = 3


def now() -> datetime:
    return datetime.now(timezone.utc)


def next_reset(t: datetime) -> datetime:
    return (t + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)


def fmt(t: datetime) -> str:
    return t.strftime("%Y-%m-%d %H:%M UTC")


class State:
    def __init__(self) -> None:
        path = Path(os.environ.get("OPEN_BUDGET_FILE", DEFAULT_FILE))
        path.parent.mkdir(parents=True, exist_ok=True)
        self.fh = open(path, "a+")
        if fcntl:
            fcntl.flock(self.fh, fcntl.LOCK_EX)
        self.fh.seek(0)
        raw = self.fh.read().strip()
        self.d = json.loads(raw) if raw else {}
        self.d.setdefault("opens", [])          # {at, job, source, outcome}
        self.d.setdefault("refused_skip", {})   # job -> date
        self.d.setdefault("paused_until", None)
        self.d.setdefault("paused_from", None)
        self.d.setdefault("test_open_needed", False)
        self.d.setdefault("last_run_start", None)

    def save(self) -> None:
        cutoff = (now() - timedelta(days=KEEP_DAYS)).isoformat()
        self.d["opens"] = [o for o in self.d["opens"] if o["at"] >= cutoff]
        self.fh.seek(0)
        self.fh.truncate()
        json.dump(self.d, self.fh, indent=1)
        self.fh.flush()

    def close(self) -> None:
        if fcntl:
            fcntl.flock(self.fh, fcntl.LOCK_UN)
        self.fh.close()


def paused(s: State, t: datetime) -> datetime | None:
    until = s.d["paused_until"]
    if until and datetime.fromisoformat(until) > t:
        return datetime.fromisoformat(until)
    return None


def test_in_flight(s: State) -> bool:
    if not s.d["test_open_needed"]:
        return False
    since = s.d.get("paused_from")
    stale = (now() - timedelta(minutes=10)).isoformat()  # a crashed session never reports back
    return any(o["outcome"] is None and o["at"] >= stale and (since is None or o["at"] >= since)
               for o in s.d["opens"])


def cmd_run_start(s: State, t: datetime) -> int:
    p = paused(s, t)
    if p:
        print(json.dumps({"go": False, "reason": f"paused until {fmt(p)}"}))
        return 0
    s.d["last_run_start"] = t.isoformat()
    s.save()
    test = s.d["test_open_needed"]
    print(json.dumps({"go": True, "opens_allowed": 1 if test else "no cap",
                      "note": "test open after a pause: 1 open only" if test else ""}))
    return 0


def cmd_open(s: State, t: datetime, job: str, source: str) -> int:
    p = paused(s, t)
    if p:
        print(f"PAUSED: no job opens until {fmt(p)}")
        return 2
    if job in s.d["refused_skip"]:
        print(f"SKIP: {job} was refused on {s.d['refused_skip'][job]}, skipped for good")
        return 3
    if test_in_flight(s):
        print("TEST: the test open after the pause has no result yet; record it first")
        return 6
    last = max((o["at"] for o in s.d["opens"]), default=None)
    if last:
        wait = SPACING_SECONDS - (t - datetime.fromisoformat(last)).total_seconds()
        if wait > 0:
            time.sleep(wait)
            t = now()
    s.d["opens"].append({"at": t.isoformat(), "job": job, "source": source, "outcome": None})
    s.save()
    print(f"OK: open {job} now")
    return 0


def cmd_result(s: State, t: datetime, job: str, outcome: str) -> int:
    pending = [o for o in s.d["opens"] if o["job"] == job and o["outcome"] is None]
    if pending:
        pending[-1]["outcome"] = outcome
    else:
        s.d["opens"].append({"at": t.isoformat(), "job": job, "source": "unrecorded",
                             "outcome": outcome})
    if outcome == "ok":
        s.d["test_open_needed"] = False
        s.save()
        print("OK: recorded")
        return 0

    s.d["refused_skip"][job] = t.date().isoformat()
    decided = [o for o in s.d["opens"] if o["outcome"] in ("ok", "refused")]
    prev = decided[-2] if len(decided) >= 2 else None
    two_in_a_row = prev is not None and prev["outcome"] == "refused" and prev["job"] != job
    if s.d["test_open_needed"] or two_in_a_row:
        until = next_reset(t)
        s.d.update(paused_until=until.isoformat(), paused_from=t.isoformat(), test_open_needed=True)
        s.save()
        why = "two different jobs refused in a row" if two_in_a_row else "test open after the pause refused"
        print(f"STOP: {why}. All job opens paused until {fmt(until)}; then one test open. "
              f"Open nothing else this run.")
        return 0
    s.save()
    print(f"SKIP: {job} refused, skipped for good. One more refusal on a different job pauses all opens.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run-start")
    o = sub.add_parser("open")
    o.add_argument("job")
    o.add_argument("--source", choices=["routine", "chat"], default="routine")
    r = sub.add_parser("result")
    r.add_argument("job")
    r.add_argument("outcome", choices=["ok", "refused"])
    sub.add_parser("status")
    pa = sub.add_parser("pause")
    pa.add_argument("--until")
    sub.add_parser("unpause")
    a = ap.parse_args(argv)

    t = now()
    s = State()
    try:
        if a.cmd == "run-start":
            return cmd_run_start(s, t)
        if a.cmd == "open":
            return cmd_open(s, t, a.job, a.source)
        if a.cmd == "result":
            return cmd_result(s, t, a.job, a.outcome)
        if a.cmd == "status":
            p = paused(s, t)
            print(json.dumps({"now": fmt(t), "paused_until": fmt(p) if p else None,
                              "test_open_needed": s.d["test_open_needed"],
                              "opens_last_3_days": len(s.d["opens"]),
                              "skipped_for_good": len(s.d["refused_skip"]),
                              "last_run_start": s.d["last_run_start"]}, indent=1))
            return 0
        if a.cmd == "pause":
            until = datetime.fromisoformat(a.until).astimezone(timezone.utc) if a.until else next_reset(t)
            s.d.update(paused_until=until.isoformat(), paused_from=t.isoformat(), test_open_needed=True)
            s.save()
            print(f"PAUSED until {fmt(until)}, then one test open")
            return 0
        if a.cmd == "unpause":
            s.d.update(paused_until=None, test_open_needed=False)
            s.save()
            print("UNPAUSED")
            return 0
    finally:
        s.close()
    return 1


if __name__ == "__main__":
    sys.exit(main())
