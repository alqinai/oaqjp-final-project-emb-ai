"""Tests of the emotion detection response and error handling."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate the five emotion categories and invalid input handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_categories(self, mock_post):
        """Check the output structure for all five dominant emotions."""
        samples = {
            "joy": "I am having so much fun today",
            "anger": "I am furious",
            "disgust": "That is disgusting",
            "sadness": "I feel very sad",
            "fear": "I am terrified",
        }
        for expected, sentence in samples.items():
            with self.subTest(emotion=expected):
                scores = dict.fromkeys(samples, 0.05)
                scores[expected] = 0.8
                mock_post.return_value = Mock(
                    status_code=200,
                    json=Mock(return_value={
                        "emotionPredictions": [{"emotion": scores}]
                    }),
                )
                result = emotion_detector(sentence)
                self.assertEqual(result["dominant_emotion"], expected)
                self.assertEqual(result[expected], 0.8)
                self.assertEqual(len(result), 6)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request_returns_none(self, mock_post):
        """HTTP 400 produces None for all six fields."""
        mock_post.return_value.status_code = 400
        result = emotion_detector("invalid")
        self.assertTrue(all(value is None for value in result.values()))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, mock_post):
        """A blank string is rejected before making an API call."""
        result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])
        mock_post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
