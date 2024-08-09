import json
from pprint import pprint
import requests

# fix for now - will actually get the json from api call
with open('_sample.json') as file:
    response = json.loads(file.read())

# ...
getProblems = lambda handle: requests.get(f'https://codeforces.com/api/user.status?handle={handle}').text

def getSolvedProblemList(handle):
    try:
        _ = getProblems(handle)
        response = json.loads(_)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(_)
        return

    # now response has everything


probset = set()
for problem in response['result']:
    if problem['verdict'] != 'OK':
        continue

    probset.add((problem['problem']['name'], problem['problem']['rating']))
    # print(problem['problem']['name'], '\t\t', problem['problem']['rating'], problem['programmingLanguage'], sep='\t')

for name, rating in probset:
    print(f'{name:<40} {rating}')



# getSolvedProblemList('qchaos')