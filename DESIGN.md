---
name: Friendship Island Scoreboard
description: A hand-painted lifeguard scoreboard strip that floats over the show slides, with a quiet sand-paper control desk behind it.
colors:
  lifeguard-red: "#d42a2a"
  lifeguard-red-deep: "#9e1c1f"
  flag-yellow: "#f6c324"
  flag-yellow-deep: "#c9971a"
  card-cream: "#fbf3df"
  weathered-plank: "#f4ead2"
  tar-ink: "#2b1d14"
  driftwood-ink: "#5a4434"
  ocean-teal: "#17a3b5"
  ocean-teal-deep: "#0f7f95"
  sand: "#ead09c"
  brass: "#c79a3e"
  desk-sand: "#efe1c0"
  desk-stroke: "#cdb88f"
  paper-white: "#ffffff"
  flamingo-pink: "#c85a8a"
  lobster-red: "#bc1c34"
  dolphin-blue: "#1a8ae2"
  seal-slate: "#6a84aa"
typography:
  numeral:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "118px"
    fontWeight: 700
    lineHeight: 1
    fontFeature: "tnum"
  money:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "92px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.01em"
    fontFeature: "tnum"
  title:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.01em"
  body:
    fontFamily: "'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: "15px"
    fontWeight: 650
    lineHeight: 1.45
  label:
    fontFamily: "'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: "13px"
    fontWeight: 650
    letterSpacing: "0.06em"
rounded:
  hardware: "6px"
  card: "8px"
  box: "12px"
  plate: "18px"
  tile: "28px"
spacing:
  hairline: "8px"
  row: "12px"
  desk: "20px"
  tile-gap: "24px"
  bar-gutter: "36px"
components:
  strip-bar:
    backgroundColor: "{colors.lifeguard-red}"
    width: "1600px"
    height: "440px"
    padding: "30px 36px"
  team-tile:
    backgroundColor: "{colors.flag-yellow}"
    rounded: "{rounded.tile}"
    padding: "28px 14px 14px"
  number-card:
    backgroundColor: "{colors.card-cream}"
    textColor: "{colors.tar-ink}"
    typography: "{typography.numeral}"
    rounded: "{rounded.card}"
    width: "96px"
    height: "146px"
  donation-plate:
    backgroundColor: "{colors.ocean-teal-deep}"
    textColor: "{colors.card-cream}"
    typography: "{typography.money}"
    rounded: "{rounded.plate}"
    height: "132px"
  leader-flag:
    backgroundColor: "{colors.lifeguard-red}"
    width: "58px"
    height: "40px"
  donor-star:
    backgroundColor: "{colors.flag-yellow}"
    width: "92px"
    height: "92px"
  desk-box:
    backgroundColor: "{colors.card-cream}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.box}"
    padding: "18px 20px"
  button:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.tar-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.card}"
    padding: "9px 14px"
  button-primary:
    backgroundColor: "{colors.lifeguard-red}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.card}"
    padding: "9px 14px"
  button-gold:
    backgroundColor: "{colors.flag-yellow}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.card}"
    padding: "9px 14px"
  button-danger-armed:
    backgroundColor: "{colors.tar-ink}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.card}"
    padding: "9px 14px"
  donation-input:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.card}"
    padding: "7px 10px"
    width: "110px"
---

# Design System: Friendship Island Scoreboard

## Overview

**Creative North Star: "The Lifeguard Scoreboard Strip"**

The projected scoreboard is one physical object: a sun-faded red plank, bolted at the corners, holding four yellow team tiles. Each tile shows the team's animal and its score on cream wooden number cards hanging from brass hooks, and below them a deep-teal plate with the team's total donations. Nothing glows, nothing is glass. Depth comes from paint over wood, soft cast shadows, brass hooks and bolts, and the weight of cards that fall and swing.

The board lives only in an always-on-top pop-out window (Document Picture-in-Picture) that floats over the fullscreen Canva deck. It carries scores and donations, nothing else. The show name, the Venmo QR, the CSA logo and the challenge timer stay on the deck's slides. The timer, the full projector window and the 2x2 board were removed on 2026-11-05.

The board speaks the show deck's language: lettering is the deck's Josefin Sans, and each team keeps its deck animal art. Points and donations are equally important, so each gets its own surface: points on yellow, money on teal.

The board is composed once on a fixed 1600x440 stage and scaled uniformly to the pop-out window, so the room always sees the same picture. Density is low and type is huge. Texture is generated, not photographed: an `feTurbulence` wood grain multiplied over the paint, bare-wood flakes masked to plank edges, and a sun-fade on the red bar.

The operator's control window is the same world at desk scale: sand-paper ground, cream boxes, Josefin Sans for headings, team adjectives in their team colors, and a plain system UI face for everything the operator reads under pressure. It borrows the palette and the display face, not the wood.

**Key Characteristics:**
- Painted wood and brass; no gradients-as-glow, no glass, no neon.
- One bold geometric face (Josefin Sans 700) for everything the audience reads.
- Points on yellow, donations on teal: the two numbers never share a surface.
- Fixed digit slots: a score never reflows, a card swaps in place.
- Change is a physical event: score cards fall off and drop on; donation totals count to their new amount.
- Fixed stage scaled to fit and clipped to its frame, never reflowed.

## Colors

Sun-faded lifeguard paint (red and flag yellow) over wood, a deep sea teal for money, near-black brown ink on cream, and the four team colors in the control view.

### Primary
- **Lifeguard Red** (lifeguard-red): the strip bar paint, the top half of the leader flag, the control view's app title and its primary action.
- **Deep Lifeguard Red** (lifeguard-red-deep): the pop-out window background behind the bar (shown only as letterbox), and the pressed edge of the primary button.

### Secondary
- **Flag Yellow** (flag-yellow): the team tiles that hold the score cards, the donor star, the leader's gold rim on the donation plate, and the Update button in the control view.
- **Deep Flag Yellow** (flag-yellow-deep): the outer edge of the donor's gold rim; stroke and pressed edge of gold buttons.

### Tertiary
- **Deep Ocean Teal** (ocean-teal-deep): the donation plate, the `$` before each donation field in the control view, and the focus ring.
- **Ocean Teal** (ocean-teal): reserved; the sea of the original board.

### Team Identity
Each team has one color, sampled from the deck's team slides. On the board, the team's animal art identifies it. In the control view, the team color paints the team's adjective.
- **Flamingo Pink** (flamingo-pink): Fierce Flamingos.
- **Lobster Red** (lobster-red): Lucky Lobsters.
- **Dolphin Blue** (dolphin-blue): Daring Dolphins.
- **Seal Slate** (seal-slate): Snazzy Seals.

### Neutral
- **Card Cream** (card-cream): number cards, donation lettering, control-view boxes, and the lower half of the leader flag (as `#fff3c4`).
- **Tar Ink** (tar-ink): score numerals and all control-view body text.
- **Driftwood Ink** (driftwood-ink): secondary control-view text (help copy, status, labels, the per-team summary line).
- **Brass** (brass): hooks, bolts, flag pole highlights.
- **Desk Sand / Desk Stroke / Paper White** (desk-sand, desk-stroke, paper-white): the control view's ground, the stroke on neutral buttons and inputs, and button and input faces.

### Named Rules
**The Paint Not Light Rule.** Color is paint on a surface. It is laid flat over wood grain and shaded by soft cast shadows. It never glows, blooms or gradients toward neon. The donor's mark is a painted gold rim and a star, not a halo. The only gradients are physical: the sun-fade on the bar, the light catching the top of the donation plate, and the curve of a cream card.

**The Two Surfaces Rule.** Yellow holds points; teal holds money. A number's surface tells the audience what it counts, before they read a `$`.

**The Two Leaders Rule.** The points leader flies the red lifeguard flag; the donations leader gets the gold rim and star. Each mark sits on the surface it rewards. Ties mark every tied team. Nobody leads at zero.

## Typography

**Display Font:** Josefin Sans (self-hosted variable woff2, weights 100-700, used at 700; falling back to Century Gothic, sans-serif)
**UI Font:** Segoe UI (system-ui stack), control view only

**Character:** A bold geometric sans carries numerals, money and control headings, matching the deck. The system UI face is reserved for operator chrome, where speed of reading beats character.

### Hierarchy
- **Numeral** (700, 118px on the 96x146 score cards; line-height 1, tabular figures): every score digit.
- **Money** (700, 92px, 0.01em, tabular figures, cream with a `4px 5px 0` deep-teal shade): the donation total. It steps down to 80px from $1,000, 72px from $10,000 and 62px from $100,000 so it stays inside the plate. While counting, the size is set for the larger of the old and new amounts, so the text never jumps mid-count.
- **Title** (700, 20-30px): control-view headings; the 24px team name in each control row; the 18px summary line ("12 pts · $2,000").
- **Body** (650 for buttons at 15px; 400 at 14px/1.45 for help copy): control view.
- **Label** (650, 13px, 0.06em, uppercase, right-aligned at a shared 10.2em width): the field labels before each control row ("Points", "Total donations").

### Named Rules
**The Back Row Rule.** If the audience reads it, it is set in Josefin Sans 700. System sans never appears on the board.

**The Tabular Rule.** Every numeral that can change uses tabular figures, so a 1 never shifts its neighbors.

## Layout

The board is a fixed 1600x440 stage, centred and uniformly scaled with `min(innerWidth/1600, innerHeight/440)`, with overflow hidden. The pop-out opens at 800x220 and the operator can resize it; letterbox space shows deep lifeguard red so it blends with the bar.

The red bar fills the stage, with 30px 36px padding and a brass bolt in each corner. It holds four equal tiles 24px apart, reading Flamingos, Lobsters, Dolphins, Seals.

Inside a tile (28px top padding for the hooks, 14px sides and foot): the top row (196px tall) holds the animal art (124x172) and two number cards 8px apart, centred with a 10px gap. The tens slot is always present; below 10 it shows a blank cream card. The animal and the cards fill the tile's width, so nothing in the row moves sideways when a flag rises. The donation plate (132px tall) runs across the foot of the tile.

The control view is a single column, at most 1100px wide, of cream boxes on desk sand: a preview of the strip (40:11) with the help text, then the score and donation box. Each team row shows the animal, the team name with a summary line, and two control rows: Points (−1, +1, +3) and Total donations (`$` field and Update). At 760px the team rows restack, art shrinks to 48px and the control rows move under the name, left-aligned.

## Elevation & Depth

Depth is physical and layered: soft, warm-brown cast shadows lift objects off what they hang on, inset highlights and shadows give planks thickness, and texture (grain, flakes) gives surfaces material. Shadows are always blurred, tinted brown-black, and fall downward. The only hard offset is the painted shade under the donation lettering.

### Shadow Vocabulary
- **Bar** (`inset 0 -10px 0 rgba(0,0,0,.14), inset 0 8px 0 rgba(255,255,255,.12)`): the red bar's thickness.
- **Tile** (`inset 0 0 0 4px rgba(150,100,10,.25), inset 0 -6px 0 rgba(150,100,10,.18), 0 8px 14px rgba(60,10,10,.35)`): the yellow tile, rimmed and lifted off the red.
- **Plate** (`inset 0 0 0 4px rgba(0,40,50,.3), inset 0 -6px 0 rgba(0,40,50,.25), 0 6px 10px rgba(40,25,10,.3)`): the donation plate set into the tile.
- **Donor rim** (`inset 0 0 0 9px #f6c324, inset 0 0 0 13px #c9971a`, plus the plate's cast shadow): the top donor's plate.
- **Hanging card** (`0 8px 10px rgba(40,25,10,.35), inset 0 0 0 3px rgba(120,90,50,.18)`): number cards.
- **Bolt** (`0 2px 3px rgba(0,0,0,.35)`): brass bolts.
- **Desk box** (`0 1px 3px rgba(90,60,30,.18), 0 10px 22px rgba(90,60,30,.16)`): control-view boxes.

### Named Rules
**The Gravity Rule.** Every shadow falls down and warm. Nothing floats on a neutral gray blur, and nothing has a zero-offset colored halo.

## Shapes

Generously eased rectangles on the board: tiles 28px, donation plates 18px, number cards 8px. Control view: buttons, inputs and number cards 8px, boxes 12px. Circles are reserved for hardware (bolts, the status dot). Recurring silhouettes are physical fixtures: two brass hooks over every number card with two punched holes, a bolt in each corner of the bar.

## Components

### Number Card (signature)
Cream card with a top-to-bottom curve (`#fffaf0` to card cream to `#f1e5c8`), two punched holes, hung from two brass hooks in a fixed 96x146 slot. On a score change the old card falls off (0.48s, accelerating, rotates 9 degrees, fades) while the new card drops from above and swings to rest (0.95s, overshoot then damped rotation 3.5 to -2 to 0.8 degrees), followed by a one-beat dashed chalk outline that fades over 1.6s.

### Donation Plate (signature)
Deep-teal painted plank across the foot of each tile, with a light catch along its top. The total is set in cream Money type. When the total changes it counts to the new amount: changes of $60 or less tick through every dollar at an even pace; larger changes ease out. The count takes 300ms plus 30ms per dollar, capped at 2.2s, and lands with one small pop (scale to 1.12 and back over 0.45s). A new update mid-count heads straight for the new total from wherever the count is. The pop-out shows the current totals without counting when it first opens.

### Team Tile
Yellow painted plank holding one team's animal, score cards and donation plate. The animal is the deck animal with its deck prop, composed by tools/compose_art.py: flamingo with the angry mark, lobster with the coin pile, dolphin with the beach ball, seal with its pixel sunglasses and sparkles.

### Leader Flag
The points leader plants a lifeguard flag (58x40, red over cream, on a 150px wooden pole) in the top-left corner of its tile. As it rises, the animal steps 12px right and 10px down and shrinks to 80% inside its own box, so the flag never covers it and the cards never move. The pole rises (0.55s), the flag unfurls (0.35s after 0.45s) and waves once (1.1s), then keeps a slow breeze ripple (3.4s loop, skew within 2.5 degrees). Losing the lead furls the flag (0.25s) and then drops the pole (0.45s).

### Donor Star
The donations leader's plate gets the gold rim, and a 92px gold star with a deep-gold outline pops onto the plate's top-right corner (0.7s overshoot from a quarter-turn). At rest it sways and swells slightly (3s loop, within 8 degrees and 110%), its shine stroke brightens in time, and a small cream sparkle flashes at its tip. Losing the lead shrinks it away (0.3s).

### Buttons (control view)
- **Shape:** gently eased (8px).
- **Default:** paper white, tar ink, 650 weight, `inset 0 0 0 2px` desk-stroke rim with a 3px bottom lip; hover warms to `#fff8e6`; active presses down 2px and drops the lip. Used for the points buttons.
- **Primary:** lifeguard red with white text and a deep-red lip; one per view (Pop out over slides / Close pop-out).
- **Gold:** flag yellow with deep-yellow rim; the Update button beside each donation field.
- **Danger:** looks default at rest; first click arms it to tar ink with "Click again to reset" for 3.5s. Resets scores and donations together.
- **Focus:** 3px deep-teal outline, 2px offset.

### Donation Field (control view)
Paper white, 2px desk-stroke border, 110px wide, right-aligned tabular figures, after a deep-teal `$`. It always holds the team's current total; the operator types the new total and presses Enter or Update. Pressing Update does not take focus from the field. Leaving the field without updating puts the saved total back. A sync from another window never overwrites the field while it has focus.

### Desk Box
Cream box, 12px radius, 18px 20px padding, desk-box shadow, Josefin Sans heading. Team rows inside are divided by a 2px dashed sand line; each row names the team with its adjective in the team's color and its noun in tar ink.

## Do's and Don'ts

### Do:
- **Do** put every score digit on a cream card in a fixed hooked slot, with tabular Josefin Sans numerals.
- **Do** keep points on yellow and donations on teal.
- **Do** make changes physical: cards fall and drop with weight; money counts up, then lands with one pop.
- **Do** keep idle motion slow and small: only the leader marks move at rest.
- **Do** build surfaces as paint over generated wood grain, with bare wood showing only at plank edges.
- **Do** honor `prefers-reduced-motion`: all animation and transition off, and totals change at once without counting.
- **Do** keep the control view in the palette and Josefin Sans, with system UI text for operator reading.

### Don't:
- **Don't** use glossy game-show panels, glowing gradients, colored halos, glass or neon.
- **Don't** let a number reflow its neighbors or change width as it updates.
- **Don't** set audience-facing text in the system sans.
- **Don't** put the show name, QR codes, logos or a timer on the board; the deck carries them.
- **Don't** let a leader mark move the score cards or cover the animal.
