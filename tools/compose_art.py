"""Compose the four team emblems for the scoreboard badges.

Sources, all from the show deck:
  src/assets/flamingo.png (clean cut-out) + assets/angry.png -> Fierce Flamingos
  src/assets/lobster.png  (clean cut-out) + assets/coins.png -> Lucky Lobsters
  src/assets/dolphin.png  (clean cut-out) + assets/ball.png  -> Daring Dolphins
  assets/seals.png (keeps the glasses) + drawn sparkles      -> Snazzy Seals

White-background sources in assets/ are cut out first (white connected to the
image edge becomes transparent, with soft edges and glows kept as partial alpha);
the src/assets cut-outs are used as they are. Everything is
arranged on a fixed canvas, trimmed to its content and saved as
src/assets/team-<name>.webp. Run:  python tools/compose_art.py
then rebuild with:  python tools/build.py
"""
import math
import pathlib

from PIL import Image, ImageDraw, ImageFilter, ImageChops

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "assets"
OUT = ROOT / "src" / "assets"
CANVAS = (900, 760)
OUT_HEIGHT = 520  # emblems are shown up to ~300px tall on the 1920x1080 stage


def cutout(name: str, flood_threshold: int = 42) -> Image.Image:
    """Remove the white background that touches the image edge."""
    im = Image.open(SRC / name).convert("RGB")
    w, h = im.size
    # pixels that are near white
    lum_min = ImageChops.darker(ImageChops.darker(*im.split()[:2]), im.split()[2])
    near_white = lum_min.point(lambda v: 255 if v >= 255 - flood_threshold else 0)
    # flood fill from the border through near-white pixels only
    region = near_white.copy()
    marker = 128
    for x in range(0, w, 4):
        for y in (0, h - 1):
            if region.getpixel((x, y)) == 255:
                ImageDraw.floodfill(region, (x, y), marker)
    for y in range(0, h, 4):
        for x in (0, w - 1):
            if region.getpixel((x, y)) == 255:
                ImageDraw.floodfill(region, (x, y), marker)
    background = region.point(lambda v: 255 if v == marker else 0)
    # grow the background mask slightly so antialiased rims get soft alpha too
    rim = background.filter(ImageFilter.MaxFilter(5))

    # colour-to-alpha against white: alpha = how far the darkest channel is from white
    darkest = lum_min
    soft_alpha = darkest.point(lambda v: min(255, int((255 - v) * 255 / max(1, flood_threshold * 2))))
    alpha = Image.composite(soft_alpha, Image.new("L", im.size, 255), rim)

    # un-blend white from the soft pixels so rims do not glow pale
    px, ap = im.load(), alpha.load()
    out = Image.new("RGBA", im.size)
    op = out.load()
    for y in range(h):
        for x in range(w):
            a = ap[x, y]
            r, g, b = px[x, y]
            if 0 < a < 255:
                k = 255 / a
                r = max(0, min(255, int(255 - (255 - r) * k)))
                g = max(0, min(255, int(255 - (255 - g) * k)))
                b = max(0, min(255, int(255 - (255 - b) * k)))
            op[x, y] = (r, g, b, a)
    return out.crop(out.getbbox())


def cutout_round(name: str) -> Image.Image:
    """Cut a round object (the beach ball) with a circular mask, so its own
    white panels stay opaque even where they touch the pale rim."""
    im = Image.open(SRC / name).convert("RGB")
    lum_min = ImageChops.darker(ImageChops.darker(*im.split()[:2]), im.split()[2])
    box = lum_min.point(lambda v: 255 if v < 238 else 0).getbbox()
    s = 4
    mask = Image.new("L", (im.width * s, im.height * s))
    ImageDraw.Draw(mask).ellipse([box[0] * s, box[1] * s, box[2] * s - 1, box[3] * s - 1], fill=255)
    mask = mask.resize(im.size, Image.LANCZOS)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out.crop(box)


def body(name: str) -> Image.Image:
    """An existing clean RGBA cut-out from src/assets."""
    im = Image.open(OUT / name).convert("RGBA")
    return im.crop(im.getbbox())


def fit(im: Image.Image, height: int) -> Image.Image:
    return im.resize((round(im.width * height / im.height), height), Image.LANCZOS)


def place(canvas: Image.Image, im: Image.Image, cx: float, cy: float, rotate: float = 0) -> None:
    if rotate:
        im = im.rotate(rotate, resample=Image.BICUBIC, expand=True)
    canvas.alpha_composite(im, (round(cx - im.width / 2), round(cy - im.height / 2)))


def sparkle(size: int) -> Image.Image:
    """Four-point yellow sparkle with a soft glow, like the deck's seal slide."""
    s = size * 2
    im = Image.new("RGBA", (s, s))
    d = ImageDraw.Draw(im)
    c = s / 2
    pts = []
    for i in range(8):
        ang = math.pi / 4 * i - math.pi / 2
        rad = size * 0.95 if i % 2 == 0 else size * 0.22
        pts.append((c + rad * math.cos(ang), c + rad * math.sin(ang)))
    glow = Image.new("RGBA", (s, s))
    ImageDraw.Draw(glow).polygon(pts, fill=(255, 236, 120, 200))
    glow = glow.filter(ImageFilter.GaussianBlur(size * 0.18))
    im.alpha_composite(glow)
    d.polygon(pts, fill=(255, 228, 92, 255))
    inner = [(c + (x - c) * 0.55, c + (y - c) * 0.55) for x, y in pts]
    d.polygon(inner, fill=(255, 250, 214, 255))
    return im


def motion_lines(w: int, h: int) -> Image.Image:
    """Three short curved speed strokes trailing behind the ball (to its right)."""
    s = 3
    im = Image.new("RGBA", (w * s, h * s))
    d = ImageDraw.Draw(im)
    for i, (y, length) in enumerate([(0.18, 1.0), (0.5, 0.8), (0.82, 0.6)]):
        x1 = w * s * length
        d.arc([0, (y - 0.5) * h * s, x1 * 2, (y + 0.5) * h * s + h * s * 0.6], 200, 250, fill=(28, 40, 60, 220), width=6 * s)
    return im.resize((w, h), Image.LANCZOS)


def save(canvas: Image.Image, name: str) -> None:
    art = canvas.crop(canvas.getbbox())
    art = fit(art, OUT_HEIGHT)
    path = OUT / f"team-{name}.webp"
    art.save(path, "WEBP", quality=88, method=6)
    print(f"wrote {path.relative_to(ROOT)} {art.size} {path.stat().st_size // 1024} KB")


def main() -> None:
    W, H = CANVAS

    # Fierce Flamingos: angry mark beside the head
    c = Image.new("RGBA", CANVAS)
    place(c, fit(body("flamingo.png"), 700), W * 0.58, H * 0.5)
    place(c, fit(cutout("angry.png"), 200), W * 0.2, H * 0.2, rotate=8)
    save(c, "flamingo")

    # Lucky Lobsters: coin pile under the claws
    c = Image.new("RGBA", CANVAS)
    place(c, fit(body("lobster.png"), 640), W * 0.42, H * 0.46, rotate=-12)
    place(c, fit(cutout("coins.png", flood_threshold=60), 300), W * 0.74, H * 0.74)
    save(c, "lobster")

    # Daring Dolphins: beach ball flying in from the left
    c = Image.new("RGBA", CANVAS)
    place(c, fit(body("dolphin.png"), 660), W * 0.64, H * 0.47)
    place(c, motion_lines(150, 110), W * 0.33, H * 0.42)
    place(c, fit(cutout_round("ball.png"), 220), W * 0.15, H * 0.46, rotate=-20)
    save(c, "dolphin")

    # Snazzy Seals: the deck's seal keeps its glasses; sparkles around it
    c = Image.new("RGBA", CANVAS)
    place(c, fit(cutout("seals.png"), 660), W * 0.5, H * 0.5)
    place(c, sparkle(78), W * 0.12, H * 0.3)
    place(c, sparkle(52), W * 0.9, H * 0.12)
    place(c, sparkle(60), W * 0.88, H * 0.78)
    save(c, "seal")


if __name__ == "__main__":
    main()
