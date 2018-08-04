# import random
# from newsapi import NewsApiClient
# from settings import api_key
#
#
# newsapi = NewsApiClient(api_key=api_key)
#
#
# def get_news_list():
#     top_headlines = newsapi.get_top_headlines(category='entertainment',
#                                           language='ru',
#                                           country='ru')
#
#     num_string = random.randint(0, 19)
#     title = top_headlines['articles'][num_string]['title']
#     url = top_headlines['articles'][num_string]['url']
#
#     return title + '\n' + url
