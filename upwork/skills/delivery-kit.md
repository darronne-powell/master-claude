# Delivery kit

> What goes to the client when a milestone or job is done. Claude writes all of it without being asked, the moment the work has passed its checks. Nothing is sent until the owner says "send".

## 1. Before the kit

- The work passed every check in `skills/project-work.md`, section 6.
- The whole thread has been read once more. Nothing the client asked for is missing.
- The client can see the result: it's live, or there's a link they can open.
- Fixed price: the milestone is funded. If it isn't, tell the owner before anything is submitted.

## 2. The pieces, in order

Each message goes in its own code block with its character count (`wc -m`). Upwork messages are unsigned and carry no payment words. Voice from section 9 of the profile.

**1. Pre-delivery message** (under 500 characters). Goes in the room just before the submission. Says the work is finished and checked, and that the submission follows in a moment with the report.

**2. Delivery message** (under 500 characters). Goes in the milestone submission box. What was done, the measured result if there is one, where to look, and that the report is attached.

**3. The report.** Written as Markdown in `clients/<slug>/reports/`, then turned into a Word file. If this Claude has a Word (docx) skill, use it. If not, hand the owner the Markdown file and say so. Sections:
- Summary, three or four lines
- Before and after, with numbers or screenshots
- What changed, item by item, against the brief
- Where the changes live (page, theme file, setting, plugin or app)
- Checks done
- How to undo it
- What the next milestone covers, when there is one

No name, signature or "prepared by" line on the report. Section 13 of the profile says which milestones get one.

**4. Post-delivery message.** Goes in the room right after the submission. The result first, in the client's terms. Then the next step from section 13: the next milestone when there is one, otherwise the strongest entry in the client's `upsells.md`. State it as what happens next ("Once Milestone 2 is funded, I'll start the same day"). Don't ask permission to carry on ("want me to start?").

**5. Feedback ask** (last milestone only). Inside the post-delivery message: offer to fix anything first, then ask for their honest feedback about working together. Asked once and never chased. Never ask for stars, a score or "5".

Hourly contract: there's no submission. The pre-delivery and delivery messages become one message in the room, with the report attached.

## 3. Sending it

1. Show the owner every piece and wait for "send".
2. On "send", in this order: post the pre-delivery message, submit the milestone with the delivery message and the report attached, post the post-delivery message.
3. Use the Upwork connector where its tool list has the step. Where it doesn't, give the owner the text and the exact clicks.
4. After each step, read the room back to confirm it landed.

The auto-reply routine never does any of this.

## 4. After it's sent

- **Proof list.** Add the job to section 6 of the profile: the link, the exact verb (built / fixed / worked on), what was done, any measured result. No amounts, and nothing the client would mind seeing in a proposal.
- **Client notes.** In `notes.md`, write what was promised against what was delivered, with the date.
- **What's next, in this order.** The upsell first, then anything in `future-work.md`, then one open ask ("Is there anything else you need a hand with, even outside the website?"). One at a time, each once per contract.
- **Closing a contract.** When a job has run its course and the client has gone quiet, the last message is short: it acknowledges where things stand, says the work does its job and offers a quick tweak on what was built if they ever need one. No pitch.

## 5. A model

An invented example: milestone 1 of 2, a slow home page on a bakery's online shop. Phone load time went from 7.8 s to 2.1 s.

Pre-delivery, in the room:
```
Hi Nora, the home page work is finished and checked on phone and desktop. I'm submitting Milestone 1 now with a short report that shows what changed, with the before and after numbers.
```

Delivery, in the submission box:
```
Milestone 1 is done. The home page now loads in 2.1 s on a phone, down from 7.8 s. I compressed and resized the banner and product photos, deferred two scripts that were blocking the page, and removed an unused slider app. Checkout and the contact form were tested after every change. The report is attached, with the steps to undo anything.
```

Post-delivery, in the room:
```
Your home page now opens in about 2 seconds on a phone, down from nearly 8, so fewer visitors should give up before they see the cakes. The product pages still carry the same heavy photos, and that's what Milestone 2 covers. Once Milestone 2 is funded, I'll start the same day and have it back to you within 48 hours.
```
