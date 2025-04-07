from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)

def fetch_news(api_key):
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_top_headlines(language='en', page_size=10)
    return articles['articles']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = 'dea097b834784195938ace34d44e6acd'  
        news_articles = fetch_news(api_key)
        if not news_articles:
            return render_template('index.html', message="No articles found.")
        else:
            return render_template('index.html', articles=news_articles)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
