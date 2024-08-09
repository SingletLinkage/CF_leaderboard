from flask import Flask, render_template
from getUserDetails import getUserList
from apiHandler import get_url_using_auth, api_custom_call
from getSolvedProblems import getSolvedProblemScore
from pprint import pprint

app = Flask(__name__)

handles = ['qchaos', 'CrazyWarlord', 'HemckerOO7', 'OutOfFuel', 'AnhadIITIAN']
method_name = 'user.info'
params = {
    'handles': ';'.join(handles)
}

# Getting Human Verification for some reason
# url = get_url_using_auth(method_name=method_name, params=params)
# response = api_custom_call(url=url)
# users = sorted(response, key=lambda user: user['rating'], reverse=True)

users = getUserList(handles=handles)
# users = sorted(users, key=lambda user: user['rating'], reverse=True)

for user in users:
    if 'lastName' not in user:
        user['lastName'] = ''
    if 'firstName' not in user:
        user['firstName'] = user['handle']

    user['score'] = getSolvedProblemScore(user['handle'])

# pprint(users)

@app.route('/')
def home_page():
    return render_template('users.html', users=users)

@app.route('/users')
def users_page():
    return render_template('new_users.html', users=users)

@app.route('/leaderboard')
def leaderboard_page():
    return render_template('contest_leaderboard.html', users=sorted(users, key=lambda user: user['rating'], reverse=True))

@app.route('/fresher-leaderboard')
def fresher_leaderboard_page():
    return render_template('prob_leaderboard.html', users=sorted(users, key=lambda user: user['score'], reverse=True))

if __name__ == '__main__':
    app.run(debug=True)
