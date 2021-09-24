import requests
import constants

tagged = 'graphql'

headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(
    constants.API_PATH,
    headers=headers,
    params={
        'site': constants.site,
        'filter': constants.filter,
        'tagged': tagged,
        'fromdate': constants.fromdate,
        'todate': constants.todate,
        'sort': constants.sort,
        'order': constants.order,
        'pagesize': constants.pagesize,
    }
)
