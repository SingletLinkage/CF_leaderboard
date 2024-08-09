import requests
import json 

handles = ['qchao123s']

getRatingList = lambda handle: requests.get(f'https://codeforces.com/api/user.rating?handle={handle}').text

response = json.loads(getRatingList(handle=handles[0]))

if response['status'] != 'OK':
    print(response['comment'])
else:
    rating_list = response['result']
    # contains json objects - contestId, contestName, handle, rank, ratingUpdateTimeSeconds, oldRating, newRating
