# /new-client

> A lead or client just appeared. Give them a file and a place on the board in two minutes, so nothing about them lives only in an inbox.

## Variables

args: $ARGUMENTS (a name, a job post link, an email, or pasted text about them; may be empty)

## What to do

1. **Gather before asking.** Read whatever the args point to. If it's a company, look at their site (Firecrawl if set up). If an email or platform connector holds the conversation, read it. Then ask only what's missing, one short question at a time:
   - name and company, how they found you (source)
   - what they want, in a sentence
   - **which language you'll work with them in** (default: the language they wrote in)
   - status: `lead` (just talking), `proposal` (you're quoting), or `active` (already agreed)
   - the next action and when

2. **Check for a duplicate** in `clients/_index.md` and `clients/*/client.md`. If they're already there, update that file instead and say so.

3. **Write `clients/<slug>/client.md`** from `clients/_template/client.md`. Slug is kebab-case from the company or person (`acme-studio`). Fill what's known, leave the rest as the template's prompts. Pricing that feels sensitive goes in `private/clients/<slug>.md` with a pointer.

4. **Add the row to `clients/_index.md`.**

5. **Ledger row:** `- YYYY-MM-DD HH:MM · <seat> · <slug>/client · New <status>: <one line>`.

6. **Offer the obvious next step in one line**, and run it on a yes: a lead with a brief → `/proposal`; an active client with a kickoff → draft the kickoff email in their language (draft only, never send without approval).
