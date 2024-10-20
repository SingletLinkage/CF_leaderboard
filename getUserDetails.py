import requests
import json
from curl_request import curl_request
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json",
    "Content-Type": "application/json",    
}

proxy = [
    {'http' : '103.130.130.130.179:8080'},
    {'http' : '134.209.67.109:19752'}
]


def getDetails(handles): 
    session = requests.session()
    _ = session.get(f'https://codeforces.com/api/user.info?handles={";".join(handles)}', headers=headers, proxies=proxy[1]).text
    session.close()
    return _ 

def getDetails_curl(handles):
    url = f'https://codeforces.com/api/user.info?handles={";".join(handles)}'
    return curl_request(url=url)


def getUserList(handles):
    # print(getDetails(handles))
    
    try:
        _ = getDetails(handles)
        response = json.loads(_)
        time.sleep(2)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(_)
        return
    
    
    if response['status'] != 'OK':
        print(response['comment'])
    else:
        return sorted(response['result'], key=lambda user: user.get('rating', 0), reverse=True)


if __name__ == '__main__':
    users = getUserList(['qchaos', 'CrazyWarlord', 'HemckerOO7', 'OutOfFuel', 'AnhadIITIAN'])
    print(users)

    # print(sorted(users, key=lambda user: user['rating'], reverse=True))




