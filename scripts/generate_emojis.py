"""Generates anti-aliased, transparent PNG emoji assets using Pillow."""

from pathlib import Path
from PIL import Image, ImageDraw

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "emojis"
SIZE = 512
FINAL_SIZE = (256, 256)


def create_base_face(color=(255, 204, 77, 255), border_color=(235, 175, 45, 255)):
    """Creates base circular face with transparent background."""
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    margin = 32
    draw.ellipse(
        [margin, margin, SIZE - margin, SIZE - margin],
        fill=color,
        outline=border_color,
        width=12,
    )
    return img, draw


def make_happy():
    img, draw = create_base_face((255, 204, 77, 255), (235, 170, 40, 255))
    dark = (85, 50, 25, 255)

    draw.arc([120, 150, 210, 230], start=190, end=350, fill=dark, width=16)
    draw.arc([302, 150, 392, 230], start=190, end=350, fill=dark, width=16)

    draw.chord([140, 230, 372, 420], start=0, end=180, fill=dark)
    draw.chord([190, 340, 322, 430], start=0, end=180, fill=(245, 110, 130, 255))
    draw.rectangle([170, 325, 342, 340], fill=(255, 255, 255, 255))

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_sad():
    img, draw = create_base_face((255, 204, 77, 255), (235, 170, 40, 255))
    dark = (85, 50, 25, 255)

    draw.ellipse([140, 190, 190, 250], fill=dark)
    draw.ellipse([322, 190, 372, 250], fill=dark)

    draw.arc([115, 130, 215, 200], start=210, end=340, fill=dark, width=12)
    draw.arc([297, 130, 397, 200], start=200, end=330, fill=dark, width=12)

    draw.arc([160, 330, 352, 450], start=200, end=340, fill=dark, width=18)
    draw.ellipse([195, 260, 225, 320], fill=(80, 180, 255, 230))

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_angry():
    img, draw = create_base_face((245, 90, 75, 255), (200, 60, 50, 255))
    dark = (60, 20, 20, 255)

    draw.line([120, 160, 220, 215], fill=dark, width=20)
    draw.line([392, 160, 292, 215], fill=dark, width=20)

    draw.ellipse([145, 215, 195, 265], fill=dark)
    draw.ellipse([317, 215, 367, 265], fill=dark)

    draw.arc([160, 330, 352, 440], start=200, end=340, fill=dark, width=18)

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_surprise():
    img, draw = create_base_face((255, 204, 77, 255), (235, 170, 40, 255))
    dark = (85, 50, 25, 255)

    draw.arc([130, 100, 210, 160], start=190, end=350, fill=dark, width=12)
    draw.arc([302, 100, 382, 160], start=190, end=350, fill=dark, width=12)

    draw.ellipse([135, 170, 205, 250], fill=(255, 255, 255, 255), outline=dark, width=10)
    draw.ellipse([155, 190, 185, 230], fill=dark)

    draw.ellipse([307, 170, 377, 250], fill=(255, 255, 255, 255), outline=dark, width=10)
    draw.ellipse([327, 190, 357, 230], fill=dark)

    draw.ellipse([216, 290, 296, 420], fill=dark)

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_fear():
    img, draw = create_base_face((255, 204, 77, 255), (235, 170, 40, 255))

    overlay = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.pieslice([32, 32, SIZE - 32, SIZE - 32], start=190, end=350, fill=(130, 175, 235, 190))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    dark = (50, 40, 70, 255)

    draw.arc([130, 130, 210, 190], start=210, end=340, fill=dark, width=14)
    draw.arc([302, 130, 382, 190], start=200, end=330, fill=dark, width=14)

    draw.ellipse([140, 190, 200, 250], fill=(255, 255, 255, 255), outline=dark, width=8)
    draw.ellipse([160, 210, 185, 235], fill=dark)

    draw.ellipse([312, 190, 372, 250], fill=(255, 255, 255, 255), outline=dark, width=8)
    draw.ellipse([327, 210, 352, 235], fill=dark)

    draw.rounded_rectangle([180, 320, 332, 400], radius=25, fill=dark)

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_disgust():
    img, draw = create_base_face((170, 205, 80, 255), (140, 175, 60, 255))
    dark = (50, 70, 30, 255)

    draw.line([130, 180, 190, 220], fill=dark, width=14)
    draw.line([130, 240, 190, 220], fill=dark, width=14)

    draw.line([382, 180, 322, 220], fill=dark, width=14)
    draw.line([382, 240, 322, 220], fill=dark, width=14)

    draw.arc([170, 300, 342, 380], start=20, end=160, fill=dark, width=16)
    draw.pieslice([220, 330, 292, 420], start=0, end=180, fill=(245, 110, 130, 255))

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def make_neutral():
    img, draw = create_base_face((255, 204, 77, 255), (235, 170, 40, 255))
    dark = (85, 50, 25, 255)

    draw.ellipse([140, 190, 190, 245], fill=dark)
    draw.ellipse([322, 190, 372, 245], fill=dark)
    draw.line([170, 350, 342, 350], fill=dark, width=16)

    return img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generators = {
        "happy.png": make_happy,
        "sad.png": make_sad,
        "angry.png": make_angry,
        "surprise.png": make_surprise,
        "fear.png": make_fear,
        "disgust.png": make_disgust,
        "neutral.png": make_neutral,
    }

    for filename, gen_func in generators.items():
        filepath = OUTPUT_DIR / filename
        image = gen_func()
        image.save(filepath, format="PNG")
        print(f"Generated: {filepath.name} ({image.size[0]}x{image.size[1]})")

    print("\nAll emoji assets generated successfully in assets/emojis/!")


if __name__ == "__main__":
    main()
