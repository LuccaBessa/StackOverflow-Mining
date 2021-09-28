import os
from pip._vendor import requests
from utils.constants import *
import time


def getData(tag, page):
    key = os.getenv('ACCESS_TOKEN')
    fromdate_timestamp = time.mktime(
        time.strptime(fromdate, '%Y-%m-%d %H:%M:%S')).__floor__()
    todate_timestamp = time.mktime(time.strptime(
        todate, '%Y-%m-%d %H:%M:%S')).__floor__()

    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(
        API_PATH,
        headers=headers,
        params={
            'site': site,
            'filter': filter,
            'key': key,
            'tagged': tag,
            'fromdate': fromdate_timestamp,
            'todate': todate_timestamp,
            'sort': sort,
            'order': order,
            'page': page,
            'pagesize': pagesize,
        }
    )

    return response.json()
