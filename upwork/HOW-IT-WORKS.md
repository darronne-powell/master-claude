# How it works

A plain guide to the system in this folder: what each part does, and what to say to use it. You don't need to open any other file. Claude reads those for you.

## The idea

Claude starts every chat with no memory of the last one, so this folder is its memory. Your niche, rates, proof and limits sit in one file, `config/profile.md`, filled in from the 15 setup questions. The other files are rules: how a proposal is written and priced, how a buyer is answered, how client work is done and delivered.

You talk in plain words and Claude picks the right rules. When it gets something wrong, tell it. A correction you give twice is written into the rules, so it stays corrected.

## 1. Winning work

Paste a job link and say "apply to this". Claude opens the job, looks at the client's site for one concrete thing to open the letter with, then writes the letter, the screening answers, a price and a boost. You read it, and it submits when you say "send".

**How the price is set.** The first letter sells one small first step, because a small yes is easier to get than a big one.

- Fixed price: the lower of the client's budget and the average bid, minus about 10%. It never goes over the budget or over the ceiling you set in setup.
- The figure sits $5 or $10 under the round number, so $340 and not $350.
- Hourly: the rate the client last paid, or the middle of their range, with "about X hours for the first step" (ten at most) and no dollar total.
- Every letter offers one small thing free, such as a first-screen mockup or one finding from their site.
- Once the buyer is talking, Claude looks for real extra scope on their site and offers it as a package beside the entry option. That's how a small first job grows.

**Volume.** The freelancer who built this system credits one thing above the rest: sending a lot of fitting proposals. Claude makes each one quick to produce, and it watches your Connects while you send them. It keeps a reserve it never goes under, caps the boost on any one proposal and skips jobs that are already crowded.

**Three ways to run it.** You picked one in setup, and you can change it by telling Claude.

- **A. Paste and send** (the default). You paste job links, Claude writes, you say "send".
- **B. Scout and draft.** A routine looks for fresh jobs every 20 minutes and saves drafts. You read them and say "send".
- **C. Submits on its own.** The routine finds, writes and submits until your Connects reach the reserve.

A routine runs only while the Claude app is open and the computer is awake. Each one is created switched off, and you switch it on yourself in the Scheduled list.

Before you choose B or C, read Upwork's current terms for connector use and its page on rate limits. One freelancer's reading in November 2026: an agent may act on a job you pointed it to, choosing and submitting jobs with no direction from you isn't allowed, and the rate-limit page says not to build automations that look for changes every few minutes, which B, C and the auto-reply all do on a timer. That's one person's reading and the rules can change, which is why A is the default.

## 2. Talking to buyers

Paste a buyer's message. The draft reply comes first, before any work, so you can answer them straight away.

- Every question gets answered, in the order asked. There are no "I'll get back to you" replies.
- When they ask for a price, the price is in that reply.
- A nudge to a quiet buyer brings something new, like a finding or a smaller first step. It's never "just checking in" and never a price cut.
- Calls follow what you chose in setup. The default is one timed live chat in the Upwork room, offered once.
- No email address, phone number or outside app goes in a message before a contract is live. Payment words stay out of Upwork messages altogether, because they can set off Upwork's off-platform warning.

The auto-reply exists only if you asked for it in setup, and it's created switched off. Once you switch it on, it answers new buyers by itself. It skips anyone you've had a contract with, and it never accepts an offer, submits a milestone or ends a contract. What it sent is in `state/auto-reply-log.md`. What it left for you is in `state/needs-owner.md`.

## 3. Doing the work

Can Claude work on Squarespace, Shopify, Wix and the rest? On most of them, yes. These platforms are web pages, and what a person can do there by clicking and typing, Claude can usually do too, in your own signed-in Chrome.

How a job goes:

1. You sign in to the client's site in Chrome, on the profile that has the Claude extension.
2. You say "take over".
3. Claude writes the client's brief as a checklist and makes sure the change can be undone (a backup, or a duplicated theme or page). Then it does the work one change at a time.
4. It checks the result the way a visitor sees it, on desktop and on a phone, and ticks the brief off item by item.

What to expect:

- You do the signing in. Claude never types a password, a 2FA code or a CAPTCHA.
- Drag-and-drop editors are slower through a browser than code, so allow for that in the dates you promise.
- Some editors block automated clicks. When that happens, Claude gives you the exact clicks and carries on from there.
- Design work needs real material: the client's images, logo and colours. Ask for them early.
- A platform you've never used yourself is slower and needs more checking. Claude says so before you quote a date.
- It works only while the Claude app and that Chrome window are open.

## 4. Delivering

When the work passes its checks, Claude writes the delivery kit without being asked:

1. A short message for the room, just before you submit.
2. The delivery message for the milestone submission box.
3. A report for the client: what changed, before and after, where the changes live and how to undo them.
4. A message for right after the submission, with the result and the next step.
5. On the last milestone, one request for honest feedback about working together. It never asks for stars or a score.

You read all of it and say "send". It goes out in that order.

## 5. After the job

Every buyer has a folder in `clients/`. As the conversation goes, Claude notes two things there: upsell ideas it spotted on their site, and anything the buyer said they want later. After a delivery it uses them in order: the upsell, then the later work, then one open question about what else they need.

Each finished job also goes on your proof list, so the next proposal can point to it.

## 6. Your profile

Say "update my profile", or name the part you want changed. Claude has two routes.

- **The Upwork connector**, for the fields it can change. In November 2026 those were the title, overview, skills, availability, intro video, employment history, education, languages and other experience.
- **The Claude extension in Chrome**, for the rest. In November 2026 that meant the portfolio, the project catalog, certifications and the hourly rate. The extension has to be on the Chrome profile where your Upwork is signed in, and signed in with the same Claude account as the app.

Upwork changes its tools, so Claude checks what the connector can do before each change. It shows you the new text first, changes one field at a time on your yes, and keeps the old version in `state/profile-history.md`.

## 7. Your week in numbers

Once a week, say "weekly numbers". You get proposals sent against your target, Connects spent, views, replies and hires, and the one thing to change this week.

- Few views: look at which jobs were picked, how late the proposals went in and how the boost was used.
- Views but few replies: the letter needs work.
- Replies but few hires: look at how those conversations went.
- All fine but slow: send more.

Give it four weeks before changing much, because one week on its own swings too much.

## What to say

| Say or paste | What you get |
|---|---|
| A job link, "apply to this" | A proposal with its price. "Send" submits it |
| A buyer's message | A draft reply. "Send" posts it |
| "Take over" | Claude works in the site you're signed in to |
| "This milestone is done" | The delivery kit |
| "Update my profile" | Profile changes, shown to you first |
| "Weekly numbers" | The week's count |
| "My rate is now..." | Your profile file is updated, and everything else follows it |
| "From now on..." | A rule of your own, kept for good |
| "What's waiting on me?" | Drafts, flags and buyers not yet answered |

## What stays yours

- Passwords, 2FA codes and CAPTCHAs.
- The word "send". From chat, nothing reaches Upwork or a client without it.
- Accepting an offer, ending a contract and giving a refund.
- Anything on a client's billing, plan, domain or user accounts.
- Switching a routine on or off.

## When something doesn't work

- **"Wrong account, no action".** The Upwork connector is signed in to a different account from the one in your profile file. Reconnect it in Settings, Connectors.
- **Claude can't see your browser.** Check the Claude extension is on the Chrome profile you're using, and signed in with the same Claude account as the app.
- **A routine didn't run.** The app was closed or the computer was asleep. It runs the next time the app opens.
- **Auto-apply stopped.** Your Connects reached the reserve. Top them up to 20 or more above it, and the routine starts again by itself on its next run.
- **Job opens are refused.** Upwork does this for a while when an account opens too many jobs too fast. Claude stops opening jobs until the next day, then tries one. Don't ask it to start sooner.

## Making it yours

The rules here came from one freelancer's account, and yours will differ. When Claude writes or prices something in a way you wouldn't, correct it in plain words. Say "from now on" and it becomes a rule at the bottom of `CLAUDE.md` that wins over the rest, apart from the safety limits. The more you correct it, the more it sounds and prices like you.
