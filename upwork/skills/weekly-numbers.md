# Weekly numbers

> One count a week, in chat, so the owner can see what the proposals are doing. Volume is the first thing it watches.

## 1. When

On the day in section 15 of the profile, or when the owner asks. If the owner opens a session on that day and this week's row is missing, offer it once. There's no scheduled task for this, and nothing checks Upwork through the week.

## 2. Where each number comes from

| Number | Source |
|---|---|
| Proposals sent | Files in `proposals/` with status SUBMITTED and a date in the week, cross-checked with `list_freelancer_proposals` |
| Connects spent | The Connects line in those files, added up, then checked against the live Connects balance |
| Viewed, replies | `list_freelancer_proposals` |
| Hires | `list_contracts`, contracts that started in the week |
| Earned | Only if section 15 says earnings are tracked. The owner gives the figure, or says to read it from the connector's financial tool |

Add up with `awk` or `python3`, never in your head. Call `list_accounts` first, as before any Upwork step.

## 3. The row

Append one row to `state/weekly-numbers.md`. Create the file with this header the first time:

| Week ending | Sent | Target | Connects | Viewed | Replies | Hires | Replies per 100 sent | Connects per reply | Earned |
|---|---|---|---|---|---|---|---|---|---|

Views and replies keep arriving after the week ends, so each pull also refreshes last week's row. Figures in this file aren't quoted anywhere outside it.

## 4. What to tell the owner

Five lines at most:
1. Proposals sent against the target. If it's under, say that first. The freelancer who built this system credits one thing above the rest: sending a lot of fitting proposals.
2. Connects spent against the budget, and how far the balance is from the reserve floor.
3. Replies per 100 sent, against the owner's own last four weeks.
4. The one thing to change this week.
5. Anything waiting on them: `state/needs-owner.md`, drafts not sent, buyers not answered.

## 5. Reading the numbers

- Few views: the job choice or the boost. Look at which posts were picked and how late the proposals went in.
- Views but few replies: the letter. Reread the three best and three worst against `skills/proposal-writer.md`.
- Replies but few hires: the room. Reread those threads against `skills/client-closer.md`.
- All fine but slow: volume. Raise the weekly target before changing anything else.

Wait for four weeks of rows before drawing a conclusion, because one week on its own swings too much. When the owner agrees a change, write it where it lives: the profile, a rulebook, or the owner's own rules in `CLAUDE.md`.
