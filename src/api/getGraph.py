from pip._vendor import requests
from utils.constants import *


def getGraph():
    tagged = 'graphql'

    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(
        API_PATH,
        headers=headers,
        params={
            'site': site,
            'filter': filter,
            'tagged': tagged,
            'fromdate': fromdate,
            'todate': todate,
            'sort': sort,
            'order': order,
            'pagesize': pagesize,
        }
    )

    return response.json()['items']
