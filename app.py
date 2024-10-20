from flask import Flask, render_template
from getUserDetails import getUserList
from getSolvedProblems import getSolvedProblemScore
from pprint import pprint
import time

app = Flask(__name__)
PROB_COUNT_START_TIME = 1723260000 # 1729449000

handles = ['qchaos', 'b23230']  # add other handles here
method_name = 'user.info'
params = {
    'handles': ';'.join(handles)
}

# Getting Human Verification for some reason
# url = get_url_using_auth(method_name=method_name, params=params)
# response = api_custom_call(url=url)
# users = sorted(response, key=lambda user: user['rating'], reverse=True)

print('Fetching Data...')  # will take quite some time depending on the number of handles
users = getUserList(handles=handles)
# users = sorted(users, key=lambda user: user['rating'], reverse=True)

for user in users:
    if 'lastName' not in user:
        user['lastName'] = ''
    if 'firstName' not in user:
        user['firstName'] = user['handle']

    user['score'] = getSolvedProblemScore(user['handle'], PROB_COUNT_START_TIME)
    print(f'Loaded data for {user["handle"]} successfully!')

print('All User data loaded!')

@app.route('/')
def home_page():
    return render_template('users.html', users=users)

@app.route('/users')
def users_page():
    return render_template('new_users.html', users=users)

@app.route('/ratings')
def ratings_page():
    return render_template('contest_leaderboard.html', users=sorted(users, key=lambda user: user['rating'], reverse=True))

@app.route('/leaderboard')
def leaderboard_page():
    return render_template('prob_leaderboard.html', users=sorted(users, key=lambda user: user['score'], reverse=True))

if __name__ == '__main__':
    app.run(debug=True)
