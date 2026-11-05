# Spec: Always-on-top scoreboard over Canva

Status: built and confirmed in Chrome over Canva, 2026-11-04. Timer-only mode skipped. Show: 2026-11-07.

## Problem

The scoreboard was built for its own projector screen: the control window sits on the laptop, and the `#display` popup goes fullscreen on the projector.

The real setup has one projector, used as the laptop's second screen. That screen runs a fullscreen Canva presentation. A normal browser window cannot stay above a fullscreen window, so the scoreboard would be hidden.

## Goal

The scoreboard floats above the fullscreen Canva presentation on the projector. The operator still drives it from the control window on the laptop.

The app stays a single offline HTML file. No build step beyond the existing `tools/build.py`, no server, no installs, no new dependencies.

## Approach

Use the **Document Picture-in-Picture API** (`documentPictureInPicture.requestWindow()`, Chrome and Edge 116+). It opens an always-on-top browser window that the page fills with its own HTML. The window stays above other windows, including a fullscreen browser tab.

The pop-out window holds one full-size `<iframe>` that loads `scoreboard.html#pip`. This reuses the existing projector view and the existing `localStorage` sync unchanged. The `#preview` iframe in the control view already uses this pattern.

Rejected:
- Rendering the board straight into the PiP document. It means refactoring `initDisplay()` to take a target window and document. More code for no visible gain.
- PowerToys "Always on Top" and an Electron wrapper. Both need an install on the show laptop.

## Changes

All code changes go in `src/scoreboard.src.html`. Run `python tools/build.py` afterwards to regenerate `scoreboard.html`.

### 1. New `#pip` mode

- `mode` gets a fourth value: `'pip'` when `location.hash === '#pip'`.
- `#pip` runs `initDisplay()`, the same as `#display`, with these differences:
  - No "Press F for fullscreen" hint. Remove `#hint`.
  - No `F` key or double-click fullscreen toggle. Fullscreen is not allowed inside a PiP window.
  - It still sends the `PING` heartbeat, so the control view's status dot works.
  - It keeps the idle cursor hide.
- The stage `fit()` already scales the 1920×1080 board to any window size. No layout change.

### 2. "Pop out over slides" button in the control bar

- This becomes the new primary button. The existing "Open projector window" becomes a secondary button, kept as the fallback.
- On click:
  1. If a pop-out is already open, focus it. Do not open a second one, because a new request replaces the old window.
  2. Call `documentPictureInPicture.requestWindow({ width: 960, height: 540 })`. The click supplies the user gesture the API needs.
  3. In the new window's document: set `html, body { margin:0; height:100%; background:#17a3b5 }`, then add one `<iframe src="{base}#pip">` sized 100% × 100% with no border.
  4. Listen for `pagehide` on the PiP window. When it fires, reset the button state.
- While the pop-out is open, the button label becomes "Close pop-out" and a click closes the window.
- If `'documentPictureInPicture' in window` is false, hide the button. Show one line instead: "Pop-out needs Chrome or Edge. Use the projector window instead."

### 3. Guard against an accidental reload

- The PiP window closes when the control tab reloads or closes. While the pop-out is open, add a `beforeunload` handler on the control window so the browser asks before leaving.
- Remove the handler when the pop-out closes.

### 4. Update the help text

Replace the help paragraph under "On the projector" with:

> Start the Canva presentation on the projector. Then click **Pop out over slides**, drag the small window onto the projector screen, and resize it. It stays on top of the slides. Close it when you need the slides alone. Do not reload this tab while it is open. Press Ctrl+Z here to undo the last score change.

### 5. Update the docs

- `PRODUCT.md`, Operating Context: replace the "Two views on one laptop" bullet. New text: the projector shows the fullscreen Canva deck, and the scoreboard floats on top of it in an always-on-top pop-out window opened from the laptop's control view.
- `.impeccable/surfaces/scoreboard-html.md`: add `#pip` next to `#display` in the mode line.

## Not in scope

- A new compact layout. The pop-out shows the existing board, scaled to the window. See open question 1.
- Moving or resizing the PiP window from code. The browser places it, and the operator drags it.
- Firefox and Safari support. They do not have the API. The old projector window stays as the fallback.

## Risks to check first

Check these on the show laptop before the other work. The first one decides whether the approach works at all.

1. **`file://` support. Resolved 2026-11-04.** Chrome 156 and Edge 156 on the show laptop report `isSecureContext: true` and expose `documentPictureInPicture` on `file://`. A click test opened the pop-out from a local file and loaded `scoreboard.html#display` in an iframe inside it. No local server needed.
2. **Stays above Canva.** Run Canva fullscreen on the projector, open the pop-out, and drag it over. Test both Canva in the browser and the Canva desktop app if the show might use it. Test Canva's presenter view too.
3. **Maximum window size.** Chrome caps the PiP window size. Measure the largest size it allows on the projector, and check whether the board reads from the back of the room at that size.
4. **Focus changes.** Click between the control window, Canva, and the pop-out. Confirm Canva stays fullscreen and the pop-out stays on top.
5. **Remembered position.** Check whether Chrome reopens the pop-out at its last position and size. If not, the operator drags it each time. Add that to the run-of-show notes.

## Acceptance

- With Canva fullscreen on the projector, the pop-out shows the live board above the slides.
- Score and timer changes in the control view show in the pop-out within about 150 ms, with the existing card animations.
- Time's-up shudder and the TIME! placard play inside the pop-out.
- The control status dot shows "open" while the pop-out is open and "not open" after it closes.
- Closing the pop-out and reopening it restores the current scores and timer.
- The control view asks before a reload while the pop-out is open.
- In a browser without the API, the pop-out button is hidden and the old projector window still works.
- `scoreboard.html` still opens from disk with no network.

## Open questions

1. **Timer-only mode.** During a challenge, the full board covers the Canva rules slide. A small timer-only layout for a screen corner would fix that. It is about 40 lines of CSS plus one toggle. Build it now or skip it?
2. **Default pop-out size.** 960×540 is a guess. Set it from the result of risk 3.
