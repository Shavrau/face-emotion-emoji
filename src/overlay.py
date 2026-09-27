"""Alpha-blended emoji overlays and HUD rendering module."""

from pathlib import Path
import cv2
import numpy as np

from src.config import ASSETS_DIR, EMOTION_EMOJI_MAP, EMOTION_LABELS


class EmojiOverlay:
    """Manages emoji asset caching and video overlay rendering."""

    def __init__(self, assets_dir: Path | str = ASSETS_DIR):
        self.assets_dir = Path(assets_dir)
        self.emojis: dict[str, np.ndarray] = {}
        self._load_emojis()

    def _load_emojis(self):
        for emotion, filename in EMOTION_EMOJI_MAP.items():
            path = self.assets_dir / filename
            if path.exists():
                img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
                if img is not None:
                    self.emojis[emotion] = img

    def draw_alpha_overlay(
        self,
        background: np.ndarray,
        overlay: np.ndarray,
        x: int,
        y: int,
    ) -> np.ndarray:
        """Blends a BGRA overlay onto a BGR background with boundary clipping."""
        bg_h, bg_w = background.shape[:2]
        ov_h, ov_w = overlay.shape[:2]

        if x >= bg_w or y >= bg_h or x + ov_w <= 0 or y + ov_h <= 0:
            return background

        x1 = max(0, x)
        y1 = max(0, y)
        x2 = min(bg_w, x + ov_w)
        y2 = min(bg_h, y + ov_h)

        ov_x1 = max(0, -x)
        ov_y1 = max(0, -y)
        ov_x2 = ov_x1 + (x2 - x1)
        ov_y2 = ov_y1 + (y2 - y1)

        overlay_crop = overlay[ov_y1:ov_y2, ov_x1:ov_x2]
        bg_crop = background[y1:y2, x1:x2]

        if overlay_crop.shape[2] == 4:
            alpha = (overlay_crop[:, :, 3] / 255.0)[:, :, np.newaxis]
            rgb = overlay_crop[:, :, :3]
            background[y1:y2, x1:x2] = (alpha * rgb + (1.0 - alpha) * bg_crop).astype(np.uint8)
        else:
            background[y1:y2, x1:x2] = overlay_crop[:, :, :3]

        return background

    def overlay_on_face(
        self,
        frame: np.ndarray,
        emotion: str,
        bbox: tuple[int, int, int, int] | list[int],
        scale: float = 1.25,
    ) -> np.ndarray:
        """Scales and centers emoji over detected face coordinates."""
        if emotion not in self.emojis or bbox is None:
            return frame

        x, y, w, h = bbox
        target_size = int(max(w, h) * scale)
        if target_size <= 0:
            return frame

        emoji_resized = cv2.resize(
            self.emojis[emotion],
            (target_size, target_size),
            interpolation=cv2.INTER_AREA,
        )

        center_x = x + w // 2
        center_y = y + h // 2
        pos_x = center_x - target_size // 2
        pos_y = center_y - target_size // 2

        return self.draw_alpha_overlay(frame, emoji_resized, pos_x, pos_y)

    def overlay_hud(
        self,
        frame: np.ndarray,
        emotion: str,
        score: float = 0.0,
    ) -> np.ndarray:
        """Renders information card in top-right corner."""
        if not emotion or emotion not in self.emojis:
            return frame

        h, w = frame.shape[:2]
        card_w, card_h = 240, 80
        margin = 15
        x1 = w - card_w - margin
        y1 = margin
        x2 = w - margin
        y2 = margin + card_h

        sub_img = frame[y1:y2, x1:x2]
        dark_rect = np.full_like(sub_img, 20)
        frame[y1:y2, x1:x2] = cv2.addWeighted(sub_img, 0.35, dark_rect, 0.65, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (80, 80, 80), 1)

        icon_size = 56
        icon = cv2.resize(
            self.emojis[emotion],
            (icon_size, icon_size),
            interpolation=cv2.INTER_AREA,
        )
        self.draw_alpha_overlay(frame, icon, x1 + 12, y1 + 12)

        label = EMOTION_LABELS.get(emotion, emotion.capitalize())
        cv2.putText(
            frame,
            label,
            (x1 + 80, y1 + 35),
            cv2.FONT_HERSHEY_DUPLEX,
            0.65,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

        confidence_pct = int(score * 100)
        cv2.putText(
            frame,
            f"Confidence: {confidence_pct}%",
            (x1 + 80, y1 + 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (200, 200, 200),
            1,
            cv2.LINE_AA,
        )

        return frame

    def apply(
        self,
        frame: np.ndarray,
        emotion: str | None,
        bbox: tuple[int, int, int, int] | list[int] | None = None,
        score: float = 0.0,
        mode: str = "both",
    ) -> np.ndarray:
        """Applies emoji overlay based on mode: 'face', 'hud', or 'both'."""
        if not emotion:
            return frame

        if mode in ("face", "both") and bbox is not None:
            frame = self.overlay_on_face(frame, emotion, bbox)

        if mode in ("hud", "both"):
            frame = self.overlay_hud(frame, emotion, score)

        return frame
