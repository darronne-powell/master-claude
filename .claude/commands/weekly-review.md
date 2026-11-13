# /weekly-review

> Fifteen minutes, once a week (Friday works). Where the pipeline stands, where the time went, how income tracks against target, and the three things that matter next week. Written to a file so the weeks add up.

## Phase 1: Gather (silently)

1. `clients/_index.md` and every client file with status `lead`, `proposal`, `active` or `paused`.
2. The last 7 days of `ledger/` rows, all seats.
3. `context/numbers.md`, `context/strategy.md`, and `private/numbers.md` if it exists.
4. Connected tools, read-only, only if they're on: platform contracts and earnings (e.g. Upwork), invoicing tool for unpaid invoices, calendar for next week's client calls, time tracker for hours.
5. Last week's review in `outputs/weekly/` if one exists, to compare.

## Phase 2: The review

Write `outputs/weekly/YYYY-Www.md` (ISO week) in English, and present it in chat in the person's language. Keep it to one screen:

1. **Pipeline:** active clients and what's due; open proposals and their age; leads gone quiet 5+ days (with a suggested follow-up for each).
2. **Proposals:** sent this week, won, lost, win rate over the last 4 weeks. One line on what the winners had in common, once there's enough data.
3. **Time:** where the week went, from the ledger (client work vs sales vs admin). Billable hours vs target if a tracker is connected.
4. **Money:** income this week/month vs target (range only in the file if exact figures are private), unpaid invoices and how overdue.
5. **Wins and lessons:** one or two lines.
6. **Next week's three:** the three things that matter most, specific and named.

## Phase 3: Act on it

- Offer to draft the follow-ups for quiet leads and overdue invoices, each in the client's language. Draft only; nothing is sent without a yes.
- Update `clients/_index.md` for anything stale (a lead that's clearly dead becomes `lost` with a reason).
- Refresh the "Current" column in `context/numbers.md`.
- If the review shows strategy drifting (e.g. the stated priority is "go direct" but every win was on a platform), say so in one line and offer to update `context/strategy.md`.
- Ledger row: `- YYYY-MM-DD HH:MM · <seat> · admin/note · Weekly review Www: <one-line headline>`.
