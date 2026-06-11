import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy_detection(self):
        """Test that joyful text returns joy as dominant emotion."""
        result = emotion_detector("I am extremely happy today!")
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_empty_input(self):
        """Test that empty input returns status code 400."""
        result = emotion_detector("")
        self.assertEqual(result["status_code"], 400)
        self.assertIn("error", result)

    def test_output_structure(self):
        """Test that all required keys exist in the output."""
        result = emotion_detector("I am sad and angry.")
        expected_keys = [
            "anger", "disgust", "fear", "joy", "sadness",
            "dominant_emotion", "status_code"
        ]
        for key in expected_keys:
            self.assertIn(key, result)


if __name__ == "__main__":
    unittest.main()