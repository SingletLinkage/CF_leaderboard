import requests
import json
from pprint import pprint

def getProxyList():
    url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=json&limit=100'

    idk = json.loads(requests.get(url).text)

    list = idk['proxies']

    proxy_list = []

    for proxy in list:
        if proxy['alive'] == True and proxy['protocol'] in ['https', 'http']:
            proxy_list.append({proxy['protocol']: proxy['proxy']})

    return proxy_list