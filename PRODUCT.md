# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Single self-contained offline HTML file (inline CSS/JS, embedded assets). Must run from the laptop with no internet, opened directly from disk. No build step, no hosting.

## Users

- **Operator:** one person at the tech table running the show from a single laptop. They change team scores and log live donations per team between and during challenges, under live-show pressure.
- **Audience:** students and guests in the ballroom watching the projected screen from a distance. They need to read the four team scores and the countdown at a glance and know which duo is which.
- **MCs:** reference the screen on stage to announce standings; they do not operate it.

## Product Purpose

A projected live scoreboard for **Friendship Island**, a charity game show presented by UMCP CSA (Chinese Student Association). Eight islanders compete as four platonic duos in puzzle races, physical challenges, and teamwork tests. The scoreboard shows each team's running point total and donation total, replacing the static "Team Score" slides in the show deck. The challenge timer stays in the deck (removed from this product 2026-11-05).

Success: the operator updates scores and donations quickly with no mistakes visible to the audience, and the audience can always see who is winning.

## Positioning

Built for one specific night and one room: the show's own teams, rules, and charity cause, running reliably offline on the show laptop. Not a general scoreboard product.

## Operating Context

- Event: Friendship Island, Nov 7, 6 PM, Stamp Colony Ballroom (University of Maryland). Dress code tropical.
- All proceeds benefit A/PI DVRP (Asian/Pacific Islander Domestic Violence Resource Project, DC).
- Runs alongside the Google Slides show deck on the same laptop; the scoreboard is shown at the deck's "Team Score" points between challenges.
- **One projector, shared with the deck.** The projector (the laptop's second screen) shows the fullscreen Canva presentation. The scoreboard floats on top of it in an always-on-top pop-out window (Document Picture-in-Picture, Chrome/Edge), opened from the control view on the laptop screen. Both views stay in sync. The standalone projector window was removed 2026-11-05; the pop-out is the only board.
- Challenges include Bird Nest x Chicken Jousting, a Lego build round (Builder/Observer, 3 minutes per round, 3 rounds, +3 perfect / +1 near match, placement bonus 10/7/4/2), and Blind Butler.
- Audience live donations ("Rose Toss": red rose = $5, white rose = $1, cash or Venmo @umcpcsa) count toward the separate Golden Friends Award. Challenge points decide "The Villa Champions". Donations are tracked per team and shown under each team's score (added 2026-11-05).

## Capabilities and Constraints

- Four teams, fixed names and animals from the deck:
  - Team 1: Fierce Flamingos
  - Team 2: Lucky Lobsters
  - Team 3: Daring Dolphins
  - Team 4: Snazzy Seals
- Per-team score with increment/decrement and direct entry; scores persist across page reloads.
- The projected board is a small pop-out beside the Canva slides, so it carries only a compact strip: per team, the animal, score and donation total. The Venmo QR and CSA logo live on the deck's own slides, not on the board (decided 2026-11-04).
- Must work fully offline from a local file; no network fonts or CDNs can be relied on at showtime.
- Must read clearly on a ballroom projector at distance.
- Existing draft: `references/Friendship_Island_Scoreboard.html` (single team-score page with 10:00 timer; its team icons do not match the deck's team animals).
- Undecided: maximum score range (not confirmed as 3 digits).

## Brand Commitments

- Name: "Friendship Island", presented as "csa presents friendship island".
- Show-specific language from the deck: islanders, duos, The Villa Champions, Golden Friends Award, Rose Toss.
- Team names and animals above are binding.
- UMCP CSA logo and A/PI DVRP name/logo appear in the deck.

## Evidence on Hand

- `references/Friendship Island Slides (IN WORK).pdf` — 36-slide show deck: title, islanders, team intros, challenge rules, score slides, donation slides, awards, thanks. Contains the Venmo QR code and CSA/DVRP logos.
- `references/Friendship_Island_Scoreboard.html` — draft scoreboard; embeds the CSA logo (as a mask image) and a background image.
- No standalone Venmo QR or logo files yet; extract from the deck or ask the user.

## Product Principles

1. **Showtime reliability first.** Offline, no dependencies, state survives a reload; nothing should fail in front of the room.
2. **Readable from the back row.** Scores and time are the content; everything else supports them.
3. **Operator never fumbles.** Controls are fast, forgiving, and kept off the projected view.
4. **Faithful to the show.** Use the deck's teams, names, and language; no invented teams, rules, or claims.
5. **The cause stays present.** The deck carries the donation QR and CSA identity; the board stays lean so it never crowds the slides it floats over.

## Accessibility & Inclusion

- Projector legibility: high contrast and large type for scores and timer.
- Teams must be distinguishable by name and animal, not by color alone.
- Respect reduced motion on the operator machine.
