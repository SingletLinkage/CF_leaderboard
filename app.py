from flask import Flask, render_template
from getUserDetails import getUserList
from apiHandler import get_url_using_auth, api_custom_call

app = Flask(__name__)

handles = ['qchaos', 'CrazyWarlord', 'HemckerOO7']
method_name = 'user.info'
params = {
    'handles': ';'.join(handles)
}

# Getting Human Verification for some reason
# url = get_url_using_auth(method_name=method_name, params=params)
# response = api_custom_call(url=url)
# users = sorted(response, key=lambda user: user['rating'], reverse=True)

# users = getUserList(handles=handles)

users = [
    {
      "country": "India",
      "lastOnlineTimeSeconds": 1723190742,
      "rating": 1340,
      "friendOfCount": 29,
      "titlePhoto": "https://userpic.codeforces.org/no-title.jpg",
      "handle": "qchaos",
      "avatar": "https://userpic.codeforces.org/no-avatar.jpg",
      "firstName": "Arka",
      "contribution": 0,
      "organization": "IIT Mandi",
      "rank": "pupil",
      "maxRating": 1340,
      "registrationTimeSeconds": 1700933170,
      "maxRank": "pupil"
    },
    {
      "lastName": "Bhola",
      "country": "India",
      "lastOnlineTimeSeconds": 1723175799,
      "city": "Delhi",
      "rating": 1203,
      "friendOfCount": 19,
      "titlePhoto": "https://userpic.codeforces.org/no-title.jpg",
      "handle": "CrazyWarlord",
      "avatar": "https://userpic.codeforces.org/no-avatar.jpg",
      "firstName": "Akshit",
      "contribution": 0,
      "organization": "IIT Mandi",
      "rank": "pupil",
      "maxRating": 1270,
      "registrationTimeSeconds": 1708105055,
      "maxRank": "pupil"
    },
    {
      "lastName": "Singh",
      "country": "India",
      "lastOnlineTimeSeconds": 1723181203,
      "rating": 1213,
      "friendOfCount": 19,
      "titlePhoto": "https://userpic.codeforces.org/3638935/title/3b388aaa15bfbb7b.jpg",
      "handle": "hemckerOO7",
      "avatar": "https://userpic.codeforces.org/3638935/avatar/1eebd2e90c9a0fb.jpg",
      "firstName": "Saurabh",
      "contribution": 0,
      "organization": "IIT Mandi",
      "rank": "pupil",
      "maxRating": 1222,
      "registrationTimeSeconds": 1700933575,
      "maxRank": "pupil"
    },
    {"lastName":"Tyagi","country":"India","lastOnlineTimeSeconds":1723189328,"city":"Ghaziabad","rating":1385,"friendOfCount":38,"titlePhoto":"https://userpic.codeforces.org/3459679/title/94009973a04b56de.jpg","handle":"mst_molik","avatar":"https://userpic.codeforces.org/3459679/avatar/7cd68859621bafcc.jpg","firstName":"Molik","contribution":0,"organization":"IIT Mandi","rank":"pupil","maxRating":1507,"registrationTimeSeconds":1694161570,"maxRank":"specialist"}
  ]

users = sorted(users, key=lambda user: user['rating'], reverse=True)

for user in users:
    if 'lastName' not in user:
        user['lastName'] = ''


@app.route('/')
def home_page():
    return render_template('users.html', users=users)

@app.route('/users')
def users_page():
    return render_template('new_users.html', users=users)

@app.route('/leaderboard')
def leaderboard_page():
    return render_template('contest_leaderboard.html', users=users)

@app.route('/fresher-leaderboard')
def fresher_leaderboard_page():
    return render_template('prob_leaderboard.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
