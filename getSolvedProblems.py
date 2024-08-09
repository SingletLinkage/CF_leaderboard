import json
from pprint import pprint
import requests

# fix for now - will actually get the json from api call
# with open('_sample.json') as file:
#     response = json.loads(file.read())

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Cookie': '_ga_K230KVN22K=GS1.1.1700933127.1.1.1700934586.0.0.0; _ga=GA1.2.520676036.1700933127; X-User-Sha1=ee038a4867f79d01c66e117af04cdaf3215754b6; 39ce7=CFGrQzj5; JSESSIONID=AEE096EC3F19AE3D0F94B497AEF5D26D; evercookie_png=zdt9yx4idbfmpex3si; evercookie_etag=undefined; evercookie_cache=undefined; 70a7c28f3de=zdt9yx4idbfmpex3si; lastOnlineTimeUpdaterInvocation=1723231685776; cf_clearance=OW8PL.F1RUSpjnUfUy7OeQ9grS78CoQJs9Y0l.9oaD4-1723230904-1.0.1.1-tQqCHvzcxr_ikOAT4vp3vMbNkVL_sMMdwrFlZkRVgn.S1IupoEJA.kzuEoUR107vNostECAVX3742Qb2kQhHcg'
}

proxy = [
    {'http' : '103.130.130.130.179:8080'},
    {'http' : '134.209.67.109:19752'}
]

def getProblems(handle): 
    session = requests.session()
    _ = session.get(f'https://codeforces.com/api/user.status?handle={handle}', headers=headers, proxies=proxy[0]).text
    session.close()
    return _

def getSolvedProblemScore(handle):
    try:
        _ = getProblems(handle)
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

        probset.add((problem['problem']['name'], problem['problem'].get('rating', None)))
        # print(problem['problem']['name'], '\t\t', problem['problem']['rating'], problem['programmingLanguage'], sep='\t')

    for name, rating in probset:
        # print(f'{name:<40} {rating}')
        if rating is not None:
            score += rating // 100

    return score

if __name__ == '__main__':
    getSolvedProblemScore('mst_molik')