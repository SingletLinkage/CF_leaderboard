import requests
import json

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


def getDetails(handles): 
    session = requests.session()
    _ = session.get(f'https://codeforces.com/api/user.info?handles={";".join(handles)}', headers=headers, proxies=proxy[1]).text
    session.close()
    return _ 


def getUserList(handles):
    # print(getDetails(handles))
    
    try:
        _ = getDetails(handles)
        response = json.loads(_)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(_)
        return
    
    
    if response['status'] != 'OK':
        print(response['comment'])
    else:
        return sorted(response['result'], key=lambda user: user['rating'], reverse=True)


if __name__ == '__main__':
    users = getUserList(['qchaos', 'CrazyWarlord', 'HemckerOO7', 'OutOfFuel', 'AnhadIITIAN'])
    print(users)

    # print(sorted(users, key=lambda user: user['rating'], reverse=True))




