from flask import Flask, render_template
from getUserDetails import getUserList
from getSolvedProblems import getSolvedProblemScore
from pprint import pprint
import time

app = Flask(__name__)
PROB_COUNT_START_TIME = 1729449000

handles = ['HoneyGupta', 'Divyansh21j', '141GHOST', 'Riddhi17', 'tvishajaiswal2696', 'Darkrai123', 'Nirupam', 'shubhamanand299', 'utkarshsahu123', 'Priansh_master', 'saurav10codes', 'EpicCoder03', 'AkshitaDangi2015', 'Ojasvijain', 'kdshacker359', 'DivyanshJindal', 'KingGarvit', 'suhavyyy', 'utkarshBansal', 'QuantumJunkie', 'Chirag352', 'gargsatvik06', 'SyntaxSorcerery', 'ArhamJain2506', 'timeless_tech_crafter', 'sakshamKundu', 'vipreshgupta', 'HellSlayer42', 'XeroRazer', 'Mr.N00B', 'JapneetKohli187', 'CP_GOD_', 'anishkumar96465213', 'ekansh007', 'mahak_ag', 'akshat_idk_29', 'anshika476', 'Akshat_ansh', 'Harmonixar', 'abhayxd', 'stellar_87', 'programmer_byte', 'ps2006', 'Dhanad', 'te_am0', 'hoda_goes_boom', 'lightman0', 'ananyaGawade', 'AmanGuptacd', 'kumaraman6012', 'Harsh_Yadav1729', 'Kartavya_Suryawanshi']
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
    return render_template('contest_leaderboard.html', users=sorted(users, key=lambda user: user.get('rating', 0), reverse=True))

@app.route('/leaderboard')
def leaderboard_page():
    return render_template('prob_leaderboard.html', users=sorted(users, key=lambda user: user.get('rating', 0), reverse=True))

if __name__ == '__main__':
    app.run(debug=True)
