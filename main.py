"""Real-Time Facial Emotion Emoji Mirror."""

import os
import warnings

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings("ignore")

import time
import cv2

from src.config import (
    CAMERA_INDEX,
    FRAME_SKIP,
    MIRROR_EFFECT,
)
from src.detector import EmotionDetector
from src.overlay import EmojiOverlay


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"Error: Unable to access camera at index {CAMERA_INDEX}.")
        return

    print("=" * 50)
    print("EMOJI MIRROR STARTED")
    print("=" * 50)
    print("Controls:")
    print("  [m] - Toggle display mode (Mask / HUD / Both)")
    print("  [f] - Toggle mirror flip")
    print("  [q] - Quit application")
    print("=" * 50)

    detector = EmotionDetector(use_mtcnn=False)
    overlay = EmojiOverlay()

    modes = ["both", "face", "hud"]
    mode_names = {"both": "Mask + HUD", "face": "Face Mask", "hud": "HUD Card"}
    current_mode_idx = 0
    mirror_enabled = MIRROR_EFFECT

    last_emotion = None
    last_score = 0.0
    last_bbox = None
    frames_since_detect = 0
    max_persist_frames = 12

    frame_count = 0
    prev_time = time.time()
    fps = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab camera frame.")
            break

        if mirror_enabled:
            frame = cv2.flip(frame, 1)

        frame_count += 1
        current_time = time.time()
        if current_time - prev_time >= 1.0:
            fps = frame_count / (current_time - prev_time)
            frame_count = 0
            prev_time = current_time

        if frame_count % FRAME_SKIP == 0:
            emotion, score, bbox = detector.get_top_emotion(frame)
            if emotion and bbox is not None:
                last_emotion = emotion
                last_score = score
                last_bbox = bbox
                frames_since_detect = 0
            else:
                frames_since_detect += 1
        else:
            frames_since_detect += 1

        if frames_since_detect > max_persist_frames:
            active_emotion = None
            active_bbox = None
            active_score = 0.0
        else:
            active_emotion = last_emotion
            active_bbox = last_bbox
            active_score = last_score

        current_mode = modes[current_mode_idx]
        frame = overlay.apply(
            frame,
            emotion=active_emotion,
            bbox=active_bbox,
            score=active_score,
            mode=current_mode,
        )

        h, w = frame.shape[:2]
        info_text = (
            f"FPS: {int(fps)} | Mode: {mode_names[current_mode]} [M] | "
            f"Mirror: {'ON' if mirror_enabled else 'OFF'} [F] | [Q] Quit"
        )
        cv2.rectangle(frame, (0, h - 30), (w, h), (15, 15, 15), -1)
        cv2.putText(
            frame,
            info_text,
            (15, h - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (220, 220, 220),
            1,
            cv2.LINE_AA,
        )

        cv2.imshow("Emoji Mirror", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("m"):
            current_mode_idx = (current_mode_idx + 1) % len(modes)
            print(f"Mode changed to: {mode_names[modes[current_mode_idx]]}")
        elif key == ord("f"):
            mirror_enabled = not mirror_enabled
            print(f"Mirror effect: {'ON' if mirror_enabled else 'OFF'}")

    cap.release()
    cv2.destroyAllWindows()
    print("Application closed.")


if __name__ == "__main__":
    main()
