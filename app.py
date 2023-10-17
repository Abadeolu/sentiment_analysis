from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
app.config["DEBBUG"] = True

analyser = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse_sentiment', methods=['POST'])
def analyse_sentiment():
    input_text = request.get_json()['input']
    sentiment = sentiment_analyzer_scores(input_text)
    return jsonify({'sentiment': sentiment})

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    # Determine the sentiment label based on the compound score
    if score['compound'] >= 0.05:
        sentiment_label = 'Positive'
    elif score['compound'] <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label

if __name__ == '__main__':
    app.run()
