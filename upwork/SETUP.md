# Setup: 15 questions

> Claude asks these one at a time, in plain English, and waits for each answer. The owner can answer any way they like: a list, a paste, links, a screenshot, a voice-note transcript. Claude turns the answers into `config/profile.md`; the owner never edits a file. "Not sure" is fine: use the default shown and mark it `(default, revisit)`.
>
> Before question 1, read the owner's live profile (`get_profile action=get`, on the account `list_accounts` confirmed). Most questions then become "your profile says this, is it right?", which is quicker for the owner. A claim on the profile goes into the proof list only after the owner confirms it's their own hands-on work.

---

## You

### 1. Who are you on Upwork?

Ask:
> What's your name exactly as clients see it on Upwork, where are you based (country and timezone), and do you have a portfolio link?

Fills: section 1. The org_uid comes from `list_accounts`.

### 2. What do you sell, and what do you never bid on?

Ask:
> In a few lines, what do you sell on Upwork? And which kinds of jobs do you never want to bid on, however good they look?

Claude then:
- Turns "what you sell" into 3 to 8 lanes (job types to bid on).
- Builds the not-in-lane list from what they refuse, plus anything clearly outside the lanes.
- Proposes 15 to 25 search keywords, most specific first and the broadest last. Show the list and let the owner add or cut.
- Sets the location filter: skip posts restricted to regions that leave out the owner's country.

Fills: sections 2, 3 and 4.

### 3. What have you worked in hands-on?

Ask:
> Which platforms and tools have you worked in yourself? Site builders (WordPress, Shopify, Squarespace, Wix, Webflow), page builders, code, design tools, anything else. And which ones do clients ask you about that you've never touched?

Claude then writes the hands-on list, yes or no per platform. Claude can work in most platforms through the browser, but taking on a "no" is the owner's call: it's never promised to a buyer before the owner agrees.

Fills: section 12.

---

## Proof and voice

### 4. What can you prove?

Ask:
> List every live site or project you can put your name to, as many as you can (aim for 10 or more). For each one: the link, what you did (built it, fixed it, sped it up, worked on part of it), and any result you measured (speed scores, load time, sales, sign-ups, errors cleared).

Claude then:
- Writes each project into the proof list with its exact verb (built / fixed / worked on). Letters may only use the verb recorded here.
- Calls `get_profile action=list_highlights` and records which portfolio items and certificates exist to attach to proposals.

Fills: sections 6 and 8. This is the answer that matters most. A thin proof list means thin letters.

### 5. What do clients say about you?

Ask:
> Paste 2 or 3 client reviews from your Upwork profile, word for word.

Claude records them as quotable, with the job type each came from. Job Success, badge and job count are never written down as fixed facts; they're re-read live before any letter quotes them.

Fills: section 7.

### 6. How do you write to clients?

Ask:
> Paste one or two proposals of yours that got replies, and two or three messages you've sent clients that sound like you. Are there words you never use?

Claude reads them for the owner's natural voice and writes 3 to 5 voice notes (sentence length, warmth, words they use, words they never use).

Default with nothing to read: plain, warm, first person, short paragraphs.

Fills: section 9.

---

## Price

### 7. What are your rates?

Ask:
> What's your hourly rate on Upwork, the lowest hourly rate you'll ever accept, and the smallest fixed-price job worth your time?

Defaults: working rate = profile rate; floor = half the profile rate; minimum fixed job $50; hourly bids capped at the profile rate unless the client has paid more before (then their last-paid rate, at most 20% over the profile rate).

Fills: section 5, the first four lines.

### 8. How should a first proposal be priced?

Ask:
> A first proposal sells one small first step, priced so it's easy to say yes to. What's the most a first proposal should ever quote (the default is $500)? Once a buyer is talking, what job size should I work toward? And what small thing are you happy to do free to open the door, like a first-screen mockup or one finding from their site?

Defaults: ceiling $500; target job value 0.6 x the ceiling; free step = a first-screen mockup for builds, one outside finding for fixes and audits.

Fills: section 5, the rest.

---

## Buyers and delivery

### 9. How do you deal with buyers?

Ask:
> Do you take calls or video with clients, or only Upwork chat? Any languages besides English? Any clients, past or current, that I must never message on my own?

Defaults: live Upwork chat only, offered once; English only; skip list empty (clients with a contract are always skipped by the auto-reply anyway).

Fills: section 10.

### 10. How fast do you deliver?

Ask:
> What's the fastest you'll promise a small job, and the longest any single milestone may take?

Defaults: small work "within 24 / 48 / 72 hours"; no milestone over 7 working days, and longer work is split into milestones.

Fills: section 10.

### 11. What goes out when a milestone is done?

Ask:
> When a milestone is finished I write the delivery messages and a short report for the client. Do you want the report on every milestone, or only the bigger ones? And after a delivery, what do you most want the buyer to do next: fund the next milestone, take a monthly care plan, or something else you sell?

Defaults: a report on every milestone; push the next milestone, and when none is left, the strongest idea noted for that client; feedback asked for on the last milestone only, once.

Fills: section 13.

---

## Tools and numbers

### 12. Where are you signed in?

Ask:
> Which Chrome profile is your Upwork signed in on? Is the Claude extension installed on that profile, signed in with the same Claude account as this app? And when a client gives you a login, where do you keep it?

Claude then:
- If the extension isn't there yet, walks the owner through adding it from the Chrome Web Store on that profile and signing in with the same Claude account.
- Checks it can see that browser, and records the profile's name.
- Never records a password, here or anywhere in this folder.

Default: one Chrome profile for Upwork and client work; the owner signs in to every site themselves.

Fills: section 14.

### 13. How many Connects can you spend?

Ask:
> How many Connects are you willing to spend in a normal week? How many should always stay in reserve? And what's the most I may spend boosting one proposal?

Defaults: no weekly figure, track only; reserve floor 20 (applying stops below it); boost cap 20 (10 for clients with unverified payment); skip jobs with more than 80 proposals.

Fills: sections 11 and 15.

### 14. How hands-off do you want it?

Ask:
> Three ways to run proposals. Which fits you?
>
> A. Paste and send. You paste job links, I write, price and show you each one, and I submit when you say "send".
> B. Scout and draft. A routine searches fresh jobs every 20 minutes and saves drafts. You read them and say "send".
> C. Submits on its own. The routine finds, writes and submits with no check from you, until your Connects reach the reserve.
>
> And do you want the auto-reply? It answers new buyers on its own once you switch it on.

Before the owner picks B or C, or says yes to the auto-reply, read them this:
> Three things to know first. This is one freelancer's reading of Upwork's rules in November 2026, so read the current rules yourself before a routine is switched on.
> 1. Upwork's terms for connector and API use allow an agent to act on a job you pointed it to. They don't allow one to choose jobs and submit to them with no direction from you, which is what C does.
> 2. Upwork's page on connector rate limits says not to build automations that look for changes every few minutes. B, C and the auto-reply all check on a timer.
> 3. An account that opens too many jobs too fast gets job opens refused for a while. The spacing script in this folder is there to prevent that, and it isn't a guarantee.

Defaults: A, paste and send. No auto-reply. Any routine is created switched off, and the owner switches it on themselves.

Fills: section 11.

### 15. What do you want counted each week?

Ask:
> Which day should I pull your weekly numbers (proposals sent, replies, hires, Connects spent)? How many proposals a week are you aiming for? And do you want your earnings tracked too?

Defaults: Sunday evening; no target yet, so the first four weeks set the baseline; earnings not tracked.

Fills: section 15.

---

## After the 15 answers

1. Write `config/profile.md` in full. Show the owner a short summary (lanes, keywords, rates, proof count, apply mode, weekly targets) and ask once: "Anything here wrong?"
2. Go back to `START-HERE.md`, step 3.
