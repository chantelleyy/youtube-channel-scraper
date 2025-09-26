from transformers import pipeline

def analyze_sentiment(comments):
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    for c in comments:
        try:
            result = sentiment_pipeline(c['text'][:512])[0]
            c['sentiment'] = result['label']
            c['sentiment_score'] = result['score']
        except Exception as e:
            c['sentiment'] = "ERROR"
            c['sentiment_score'] = 0.0
    return comments