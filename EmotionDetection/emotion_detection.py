import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends the provided text to the Watson Emotion Prediction API
    and returns the raw response text containing emotion analysis.
    
    Parameters:
        text_to_analyze (str): The text that needs to be analyzed.
    
    Returns:
        str: The response text returned by the Watson API.
    """
    # URL endpoint for the Watson Emotion Prediction service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
     # Required header specifying the emotion analysis model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # JSON payload containing the text to analyze
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=payload, headers=headers)

        # Handle blank input / API error
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response_dict = json.loads(response.text)

    # Extract the emotion scores
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }