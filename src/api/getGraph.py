import os
from pip._vendor import requests
from utils.constants import *


def getGraph(page):
    key = os.getenv('ACCESS_TOKEN')
    tagged = 'graphql'

    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(
        API_PATH,
        headers=headers,
        params={
            'site': site,
            'filter': filter,
            'key': key,
            'tagged': tagged,
            'fromdate': fromdate,
            'todate': todate,
            'sort': sort,
            'order': order,
            'page': page,
            'pagesize': pagesize,
        }
    )

    return response.json()
