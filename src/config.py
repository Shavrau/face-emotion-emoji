"""Global configuration and emotion-to-asset mappings."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets" / "emojis"

CAMERA_INDEX = 0
FRAME_SKIP = 2
MIRROR_EFFECT = True

EMOTION_EMOJI_MAP = {
    "happy": "happy.png",
    "sad": "sad.png",
    "angry": "angry.png",
    "surprise": "surprise.png",
    "fear": "fear.png",
    "disgust": "disgust.png",
    "neutral": "neutral.png",
}

EMOTION_LABELS = {
    "happy": "Happy 😄",
    "sad": "Sad 😢",
    "angry": "Angry 😡",
    "surprise": "Surprise 😲",
    "fear": "Fear 😨",
    "disgust": "Disgust 🤢",
    "neutral": "Neutral 😐",
}


def get_emoji_path(emotion: str) -> Path | None:
    """Returns absolute path to emoji file if found, otherwise None."""
    filename = EMOTION_EMOJI_MAP.get(emotion.lower() if emotion else "")
    if filename:
        path = ASSETS_DIR / filename
        if path.exists():
            return path
    return None
