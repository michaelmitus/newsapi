import pprint
import json
import requests
from newsapi import NewsApiClient

# pip install newsapi-python

def top_news(**kwargs):
    all_articles = newsapi.get_top_headlines(
        q = kwargs['q'],
        sources = kwargs['sources'],
        page_size = kwargs['page_size'],
        page = kwargs['page']
    )
    articl = all_articles['articles']
    for news_number in range(0, news_on_page):
         if all_articles['totalResults'] == news_number :
            break
         print(articl[news_number]['title'])

def list_of_filters(params, **filters):
    all_sources = newsapi.get_sources(country = filters['country'],
                                      language = filters['language'],
                                      category = filters['category'])
    sources = all_sources['sources']
    selections = set()
    for news_number in range(0, len(all_sources['sources'])):
        selections.add(sources[news_number][params])
    print('Select '+params)
    for news_number in range(0, len(selections)):
        print(str(news_number+1)+'. '+list(selections)[news_number])
    print('0. None')
    print('')
    choose = int(input('Enter the selection number: '))
    print('---')

    if choose == 0:
        return None
    else:
        return(str(list(selections)[choose-1]))

def all_news(**kwargs):

    all_sources = newsapi.get_sources(
        category = kwargs['category'],
        language = kwargs['language'],
        country = kwargs['country'] )

    sources = all_sources['sources']
    if all_sources['sources']:
        print('News list:')
        for news_number in range(0, news_on_page):
             if news_number == len(all_sources['sources']) :
                 break
             print(sources[news_number]['description'])
    else:
        print('No news')

def print_all_news():
    category_param = list_of_filters('category', country=None, language=None, category=None)
    language_param = list_of_filters('language', country=None, category=category_param, language=None)
    country_param = list_of_filters('country', category=category_param, language=language_param, country=None)
    all_news(category=category_param, language=language_param, country=country_param)

def search_by_request():
    top_news(q = raw_input('Enter request: '), page_size=10, page=1, sources='bbc-news')

news_on_page = 10

api_key = 'c6b4dff59361415dada7968f05685325'

newsapi = NewsApiClient(api_key)

print_all_news()
#search_by_request()