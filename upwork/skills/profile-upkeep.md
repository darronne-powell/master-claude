# Profile upkeep

> Keeping the owner's Upwork profile current. Two routes: the Upwork connector for what it can change, and the Claude extension in Chrome for the rest.

## 1. Two routes

**The connector first.** Check what it can do today: call its `get_tool_help`, or read the actions on `update_profile`. As seen in November 2026 it could change the title, the overview, the skills list, availability and the intro video, and add, edit or remove employment, education, languages and other experience. Every change comes back as a preview. Confirm it only on the owner's yes.

**Chrome for the rest.** As seen in November 2026 the connector had no action for the portfolio, the project catalog, certifications or the hourly rate. Tools change, so check again before assuming. For these:
1. The Claude extension is installed on the Chrome profile where Upwork is signed in (section 14), signed in with the same Claude account as this app.
2. The owner signs in to Upwork themselves if the session has ended.
3. Check the name on the profile page matches section 1 before any edit.
4. Edit the way a person would: open the item, change the field, save, read it back.
5. If the extension can't drive a file upload dialog, the owner picks the file and you carry on from there.

## 2. How a change is made

1. Save the current text, with the date, in `state/profile-history.md`.
2. Show the new version in a code block with its character count.
3. Change one field at a time, on the owner's yes.
4. Read the field back from the live profile to confirm it saved.

The rate, title and overview are never changed as a side effect of another job. The routines never touch the profile.

## 3. What to keep current

After every job that ships:
- A portfolio item when the work can be shown: a clean image with no one else's name or credit on it, the client's permission where it's needed, and a line on what the owner did.

Once a month, read the live profile and check:
- The title carries the main words of the owner's lanes (section 2).
- The first two lines of the overview say who the owner helps and with what. The opening is what a buyer sees before clicking through.
- Skills are ordered by the work the owner is winning now.
- Employment and education are true and current.
- The strongest two portfolio items come first.
- Each catalog project matches a lane, and its price fits section 5.

Only claim work the owner did hands-on. A number on the profile needs a source the owner can show.

## 4. Notes from doing it (November 2026, check they still hold)

- Visitors who weren't signed in saw only the first two portfolio items, so order matters.
- The project catalog accepted one price tier or three.
- The catalog's image crop frame opened small. Drag it to the corners before saving.
