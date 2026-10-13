# Emotion Detector — IBM Watson NLP + Flask

Final project for IBM's **Developing AI Applications with Python and Flask** course.

This application analyzes text for five emotions: anger, disgust, fear, joy, and sadness. It displays each score and identifies the dominant emotion using IBM Watson NLP.

## Files
- `EmotionDetection/emotion_detection.py`: Watson NLP API integration and formatted results
- `EmotionDetection/__init__.py`: Python package
- `test_emotion_detection.py`: unit tests with mocked Watson responses
- `server.py`: Flask server with blank-input error handling
- `templates/index.html`, `static/`: web interface

## Run

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -v
python3 -m pylint server.py
python3 server.py
```

Browse to http://127.0.0.1:5000 and enter text, e.g. `I am having so much fun today`.

**Note:** The IBM Watson Skills Network service may only be available within the course lab. Mocked tests verify formatting and error-handling logic, but the live Watson response and deployment screenshots must be tested in an environment with access to the service.
