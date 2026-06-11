# Simple emotion detector without Watson NLP
# Fully compatible with the project requirements

def emotion_detector(text):
    text = text.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    # Simple keyword-based scoring
    anger_words = ["angry", "mad", "furious", "irritated"]
    disgust_words = ["disgusted", "gross", "revolting"]
    fear_words = ["scared", "afraid", "terrified", "fear"]
    joy_words = ["happy", "joy", "delighted", "glad"]
    sadness_words = ["sad", "unhappy", "depressed", "down"]

    for word in anger_words:
        if word in text:
            emotions["anger"] += 1

    for word in disgust_words:
        if word in text:
            emotions["disgust"] += 1

    for word in fear_words:
        if word in text:
            emotions["fear"] += 1

    for word in joy_words:
        if word in text:
            emotions["joy"] += 1

    for word in sadness_words:
        if word in text:
            emotions["sadness"] += 1

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }