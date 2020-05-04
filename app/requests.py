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

