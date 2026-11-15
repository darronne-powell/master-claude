# Project work

> How client work gets done inside the client's own platform: WordPress, Shopify, Squarespace, Wix, Webflow or any other tool that runs in a browser. The owner signs in, says "take over", and Claude does the work in that tab through the Claude extension in Chrome.

## 1. The idea

Most site builders and dashboards are web pages. If a person can do a job there by clicking and typing, Claude can usually do it there too, in the owner's own signed-in browser. Nothing has to be installed on the client's side.

Three things stay with the owner: signing in, any decision the brief doesn't cover, and the word "send" on everything the client sees.

## 2. Before touching anything

1. **Write the brief down.** In `clients/<slug>/notes.md`, list what the client asked for as a numbered checklist, in their words. Read the whole thread and every attachment first. If a document has a later version, the latest one is the brief.
2. **Name what's unclear.** One list of open questions for the owner. Don't guess at a client's intent on something that can't be undone.
3. **Check the hands-on list** (section 12 of the profile). A platform marked "no" can still be worked on, but only after the owner hears it'll be slower and says yes.
4. **Check the contract.** Fixed price: the milestone is funded. Hourly: the contract is active. If not, tell the owner before any work.

## 3. Getting in

- The owner signs in to the client's site in the Chrome profile named in section 14, then says "take over".
- Before the first click, check you're in the right browser and on the right account: the site name, and the signed-in user shown in the dashboard.
- An expired session, a 2FA prompt or a CAPTCHA: stop and ask the owner to handle it. Never type a password, never write one down, never repeat one back.
- Work in one tab the owner can watch. Close any tab you opened when the work is done.

## 4. Safety net first

Before the first change, make sure it can be undone.

| Platform | Before you edit |
|---|---|
| WordPress | A full backup from the host panel or a backup plugin. Use staging where the host offers it. Copy a page before a big edit to it, and know where its revisions are. |
| Shopify | Duplicate the live theme and work on the copy. Publish only after the owner's yes. |
| Squarespace | There's no staging. Duplicate the page, edit the copy and swap it in when approved. Site-wide style changes go live when saved, so note the old values first. |
| Wix | Changes stay in the editor until Publish. Site History can restore an earlier version. |
| Webflow | Changes stay in the Designer until Publish. An earlier version can be restored from the site settings. |
| Anything else | Look for version history, an export or a duplicate button. If there's none, write the old values into `notes.md` before changing them. |

These are starting points. Plans and versions differ, so check what this site offers before relying on it. On most platforms, content edited in the dashboard (products, posts, bookings, menus) goes live the moment it's saved.

## 5. Doing the work

- **Look first.** Open the live page and the editor side by side. Note how the site is built (theme, page builder, apps) before changing anything.
- **One change at a time.** Make it, check it on the front end, then the next. Ten changes with one fault among them are slow to untangle.
- **Stay inside the brief.** Something else that's broken or weak goes into the client's `upsells.md`. Don't fix it quietly and don't ignore it.
- **Don't delete.** Hide, unpublish or duplicate. A delete is the owner's click.
- **No side effects.** No plugin, app or theme updates, installs or removals unless the brief asks for them.
- **Hands off the account.** Billing, plan, domain, DNS and user pages stay closed unless the brief is about them and the owner said so in this conversation.
- **Use the exact route when there is one.** A custom CSS or code panel, an import tool or the platform's own API is quicker and more exact than dragging things around a visual editor. Use it when the owner's login reaches it.
- **Proof as you go.** Save a before and an after screenshot of each change in `clients/<slug>/screenshots/` when the browser tool can save one. Otherwise note the before and after values in `notes.md`.
- **Hourly contracts.** Note the time each piece of work took in `notes.md`. The owner logs it on Upwork.

## 6. Checking it

Work isn't done until it's checked the way a visitor sees it.

1. Signed out, or in a private window, with the site's cache cleared.
2. At desktop width and at phone width.
3. Every form, button, checkout or booking step the change touched, tested once. Use the platform's test mode for a checkout. Never place a real order.
4. Nothing else moved: look over the pages around the change.
5. The brief, item by item. Each line in `notes.md` gets "done, checked" or the reason it isn't.
6. The whole thread once more, for anything asked along the way that never made the checklist.

Anything that fails goes back to section 5 before the owner hears "done".

## 7. Limits

- Drag-and-drop editors are slower through a browser than code. Allow for it in the dates the owner promises.
- Some editors block automated clicks or behave oddly under them. When that happens, give the owner the exact clicks to make and carry on from there.
- Good design needs real material: the client's images, logo, colours and fonts. Ask for them early. Don't fill a page with placeholders and call it finished.
- A platform the owner has never used means slower work and more checking. Say so before the owner quotes a date.
- Claude works only while the app and that Chrome window are open.

## 8. While you work

Note upsell ideas in `upsells.md` and anything the client says they'll want later in `future-work.md`, as they come up. When the last item is checked, go straight to `skills/delivery-kit.md` without being asked.
