import pprint
import json
import requests
from newsapi import NewsApiClient

# pip install newsapi-python

news_on_page = 10

api_key = 'c6b4dff59361415dada7968f05685325'

newsapi = NewsApiClient(api_key)

def list_of(params):
    all_sources = newsapi.get_sources()
    sources = all_sources['sources']
    langs = set()
    for news_number in range(0, len(all_sources['sources'])):
        langs.add(sources[news_number][params])
    print(params+'s list: ')
    for news_number in range(0, len(langs)):
        print(str(news_number+1)+'. '+list(langs)[news_number])
    print('0. None')
    print('')
    choose = int(input('Please: '))
    if choose == 0:
        return None
    else:
        return(str(list(langs)[choose-1]))

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

def all_news(**kwargs):
    all_sources = newsapi.get_sources(
        category = kwargs['category'],
        language = kwargs['language'],
        country = kwargs['country'] )

    sources = all_sources['sources']
    if all_sources['sources']:
        for news_number in range(0, news_on_page):
             if news_number == len(all_sources['sources']) :
                 break
             print(sources[news_number]['description'])
    else:
        print('No news')

#languages_list()
#list_of('language')
#list_of('country')
all_news(category=list_of('category'),language=list_of('language'),country=list_of('country'))
#top_news(q = 'war', page_size=10, page=1, sources='bbc-news')