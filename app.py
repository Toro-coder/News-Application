from flask import Flask, render_template

from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def home():
    # client id and api_key for authentication
    newsapi = NewsApiClient(api_key="3addb2a0f78e4697a0f96c1333b4bc69")
    all_articles = newsapi.get_everything(sources="bbc-news")

    # top headlines
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')

    # fetching all the articles
    t_articles = top_headlines['articles']
    # fetch all the articles news
    a_articles = all_articles['articles']

    news = []
    des = []
    img = []
    p_date = []
    url = []

    # fetching the contents of the articles
    for i in range(len(t_articles)):
        main_article = t_articles[i]

        # appending the contents inthe list
        news.append(main_article['title'])
        des.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

    news_all = []
    des_all = []
    img_all = []
    p_date_all = []
    url_all = []

    for i in range(len(a_articles)):
        main_all_article = a_articles[i]

        # appending the contents in the list
        news_all.append(main_all_article['title'])
        des_all.append(main_all_article['description'])
        img_all.append(main_all_article['urlToImage'])
        p_date_all.append(main_all_article['publishedAt'])
        url_all.append(main_all_article['url'])

        contents = zip(news, des, img, p_date, url)
        all = zip(news_all, des_all, img_all, p_date_all, url_all)

    return render_template('home.html', contents=contents, all=all)


if __name__ == '__main__':
    app.run(debug=True)
