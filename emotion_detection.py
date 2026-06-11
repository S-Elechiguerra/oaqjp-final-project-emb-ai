import watson_nlp

# Load the Watson NLP emotion model
emotion_model = watson_nlp.load('emotion_aggregated-workflow_en_stock')


def emotion_detector(text):
    """
    Detects emotions in the input text using Watson NLP.
    Returns a formatted dictionary with emotion scores,
    dominant emotion, and status code.
    """

    # Task 7: Error handling for blank input
    if not text or text.strip() == "":
        return {
            "error": "Input text is empty.",
            "status_code": 400
        }

    # Run the Watson NLP model
    result = emotion_model.run(text)
    result_dict = result.to_dict()

    # Extract emotion scores
    emotions = result_dict["emotion_predictions"][0]["emotion"]

    # Determine dominant emotion
    dominant = max(emotions, key=emotions.get)

    # Task 3: Required formatted output
    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant,
        "status_code": 200
    }