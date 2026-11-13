# /proposal

> Turn a job post, brief or RFP into a proposal that sounds like you, prices like you, and is written in the client's language. Claude drafts. You submit.

## Variables

args: $ARGUMENTS (a job post URL, pasted job text, a client slug, or empty)

## FOR CLAUDE

- **Never submit, send or post anything.** Not on Upwork, not on Malt, not by email. The output is a draft file and a copy-ready block. Submitting spends the person's connects, money or reputation, so it is always their click.
- **Unlisted tools are not a mismatch.** Darronne uses more premium tools than `context/you.md` lists. If a job names a tool that isn't listed, still treat it as a fit; ask Darronne "do you use X?" before the proposal names it, then add it to `context/you.md`.
- **Ask Darronne for the portfolio pieces to attach before the proposal is final** (video links, samples). Standing instruction from /install, 2026-11-13. Never invent or guess proof.
- Writing follows `reference/writing-style.md`. No "I hope this message finds you well", no "Je me permets de vous contacter". Open with their problem, not your biography.

## Phase 1: Read the job (silently)

1. Get the full brief. URL → fetch it (Firecrawl if set up; a connector if the platform has one). Pasted text → use it. A client slug → read `clients/<slug>/client.md`.
2. Pull out: the actual problem, deliverables, budget or rate range, timeline, required skills, screening questions, red flags (vague scope, "quick and easy", rate far below the floor, asks for free work, wants contact off-platform before a contract).
3. **Detect the language** of the brief. That's the proposal language unless the client file says otherwise.

## Phase 2: Fit check (say it in 3-4 lines)

Read `context/services.md`, `context/practice.md`, `context/platforms.md`, and `portfolio/`. Then tell the person, in their chat language:

- **Fit:** strong / partial / poor, and why in one line.
- **Price:** what you'd quote and how it compares to their budget and `services.md`'s rate floor. If the budget is below the floor, say so plainly and suggest either a smaller scope at the right price or skipping it.
- **Red flags,** if any.
- **Recommend:** go / go with changes / skip.

Wait for a go. A skip gets a ledger `note` row (so the pattern of skipped jobs is visible later) and stops here.

## Phase 3: Draft

Write `proposals/YYYY-MM-DD-<client-or-job-slug>.md` containing:

1. **The proposal**, in the client's language, sized to the platform (Upwork: short, the first two lines visible in the preview must hook; email/RFP: can be longer and structured). Structure:
   - Their problem, restated sharply in one or two lines (proves you read it)
   - How you'd solve it: approach in 3-5 concrete steps
   - Proof: the one or two most relevant pieces from `portfolio/` or past clients, with a result
   - Price and timeline, with what's included and what isn't (from `services.md` scope rules)
   - One specific question that moves the conversation forward
2. **Answers to any screening questions**, each separately.
3. **Notes for you** (in English): price rationale, risks, what to watch for.

Show the proposal in chat as a copy-ready block. Ask for edits; revise until approved.

## Phase 4: File it

1. If this client isn't on the board, run the `/new-client` steps (status `proposal`). If they are, set status to `proposal` and next action to "await reply, follow up <date + 3 working days>".
2. Link the proposal file from the client file's Log.
3. Ledger row: `- YYYY-MM-DD HH:MM · <seat> · <slug>/ship · Proposal drafted: <job>, <price>`. When the person confirms they submitted it, add a second row and update the client file.
4. Over time, mark proposals won or lost in the client file. `/weekly-review` uses those to compute the win rate and learn which openings work.
