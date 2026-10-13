"""Analyze emotions using the IBM Watson NLP EmotionPredict service."""

import requests

SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the required empty result for invalid input."""
    return {**dict.fromkeys(EMOTIONS), "dominant_emotion": None}


def emotion_detector(text_to_analyze):
    """Return emotion scores and dominant emotion in a six-key dictionary."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    response = requests.post(
        SERVICE_URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers=HEADERS,
        timeout=20,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    scores = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(EMOTIONS, key=result.get)
    return result
