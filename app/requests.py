from app import app
import urllib.request,json
from .models import NewsSource, Article

Source = NewsSource


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
source_url = app.config["SOURCE_API_BASE_URL"]

#Getting the article url
article_url = app.config["ARTICLE_BASE_URL"]



def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url= source_url.format(category, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response=json.loads(get_source_data)
        source_results = None
        if get_source_response['sources']:
            source_results_list=get_source_response['sources']
            source_results=process_sources(source_results_list)
    return source_results

def process_sources(source_results):
    '''
    Function  that processes the Newssource_results and transform them to a list of Objects
    Args:
        Newssource_list: A list of dictionaries that contain news sources
    Returns :
       Newssource_results: A list of news objects
    '''
    source_list = []
    for source_item in source_results:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url= source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        if name:
            new_source= Source(id,name,description,url,category,language,country)
            source_list.append(new_source)
    return source_list


def get_article(source_id):
    get_article_url = article_url.format(source_id, api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_results):
    articles = []
    for article in article_results:
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")
        if urlToImage:
            new_article = Article(title,description,url,urlToImage,publishedAt)
            articles.append(new_article)
    return articles

