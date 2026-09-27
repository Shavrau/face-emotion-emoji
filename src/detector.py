"""Facial expression and emotion detection module."""

from fer import FER


class EmotionDetector:
    """Facial emotion recognition wrapper using FER."""

    def __init__(self, use_mtcnn: bool = False):
        self.detector = FER(mtcnn=use_mtcnn)

    def detect_emotions(self, frame):
        """Returns detected faces with bounding boxes and emotion probabilities."""
        return self.detector.detect_emotions(frame)

    def get_top_emotion(self, frame):
        """
        Analyzes the frame and returns dominant emotion and coordinates for primary face.
        Returns: (emotion, score, bbox)
        """
        results = self.detector.detect_emotions(frame)
        if not results:
            return None, 0.0, None

        first_face = results[0]
        bbox_raw = first_face.get("box")
        bbox = tuple(int(v) for v in bbox_raw) if bbox_raw is not None else None
        emotions = first_face.get("emotions", {})

        if not emotions:
            return None, 0.0, bbox

        top_emotion = max(emotions, key=emotions.get)
        top_score = emotions[top_emotion]

        return top_emotion, top_score, bbox
