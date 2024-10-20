import json
from pprint import pprint
import requests
from curl_request import curl_request
from getProxyList import getProxyList
import random
import time

# fix for now - will actually get the json from api call
# with open('_sample.json') as file:
#     response = json.loads(file.read())

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
}
proxy = random.choice(getProxyList())

def getProblems(handle): 
    session = requests.session()
    _ = session.get(f'https://codeforces.com/api/user.status?handle={handle}', headers=headers, proxies=proxy).text
    session.close()
    return _

def getProblems_curl(handle):
    url = f'https://codeforces.com/api/user.status?handle={handle}'
    return curl_request(url=url)

def getSolvedProblemScore(handle, afterTime=0):
    try:
        # _ = getProblems_curl(handle)
        _ = getProblems(handle)
        time.sleep(2)
        response = json.loads(_)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(_)
        return

    # print(response)
    # now response has everything

    probset = set()
    score = 0
    for problem in response['result']:
        if problem['verdict'] != 'OK':
            continue
        
        if problem['creationTimeSeconds'] < afterTime:
            continue


        probset.add((problem['problem']['name'], problem['problem'].get('rating', None)))
        # print(problem['problem']['name'], '\t\t', problem['problem']['rating'], problem['programmingLanguage'], sep='\t')

    for name, rating in probset:
        # print(f'{name:<40} {rating}')
        if rating is not None:
            score += 50 + 4 * int((rating-800)**2 // 6400)
            # score += int(1.5**(rating - 800 // 100))

    return score

if __name__ == '__main__':
    print(getSolvedProblemScore('CrazyWarlord', 1723264494))