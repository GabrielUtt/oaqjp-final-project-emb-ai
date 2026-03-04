"""
server.py

Flask web application for Emotion Detection.
Provides routes for rendering index page and detecting emotions in text input.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the main HTML page for user input.
    
    Returns:
        str: Rendered HTML template 'index.html'.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    This function handles requests sent to /emotionDetector.
    It extracts the user input, calls the emotion_detector function,
    and formats the response as required.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
