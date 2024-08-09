import requests
import json

getDetails = lambda handles: requests.get(f'https://codeforces.com/api/user.info?handles={";".join(handles)}').text


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
    getUserList(['qchaos', 'mst_molik', 'CrazyWarlord'])

    
    users = [
    {
        'avatar': 'https://userpic.codeforces.org/no-avatar.jpg',
        'contribution': 10,
        'country': 'India',
        'firstName': 'Arka',
        'friendOfCount': 29,
        'handle': 'qchaos',
        'lastOnlineTimeSeconds': 1723190742,
        'maxRank': 'pupil',
        'maxRating': 1340,
        'organization': 'IIT Mandi',
        'rank': 'pupil',
        'rating': 1340,
        'registrationTimeSeconds': 1700933170,
        'titlePhoto': 'https://userpic.codeforces.org/no-title.jpg'
    },
    {
        'avatar': 'https://userpic.codeforces.org/no-avatar.jpg',
        'contribution': 5,
        'country': 'United States',
        'firstName': 'John',
        'friendOfCount': 112,
        'handle': 'johndoe123',
        'lastOnlineTimeSeconds': 1723190341,
        'maxRank': 'specialist',
        'maxRating': 1520,
        'organization': 'MIT',
        'rank': 'specialist',
        'rating': 1485,
        'registrationTimeSeconds': 1690930112,
        'titlePhoto': 'https://userpic.codeforces.org/no-title.jpg'
    },
    {
        'avatar': 'https://userpic.codeforces.org/no-avatar.jpg',
        'contribution': 0,
        'country': 'Russia',
        'firstName': 'Ivan',
        'friendOfCount': 300,
        'handle': 'ivan_the_coder',
        'lastOnlineTimeSeconds': 1723190655,
        'maxRank': 'candidate master',
        'maxRating': 2100,
        'organization': 'Moscow State University',
        'rank': 'expert',
        'rating': 2040,
        'registrationTimeSeconds': 1680932198,
        'titlePhoto': 'https://userpic.codeforces.org/no-title.jpg'
    },
    {
        'avatar': 'https://userpic.codeforces.org/no-avatar.jpg',
        'contribution': 15,
        'country': 'China',
        'firstName': 'Wei',
        'friendOfCount': 500,
        'handle': 'wei_supercoder',
        'lastOnlineTimeSeconds': 1723190123,
        'maxRank': 'grandmaster',
        'maxRating': 2800,
        'organization': 'Tsinghua University',
        'rank': 'grandmaster',
        'rating': 2750,
        'registrationTimeSeconds': 1670931170,
        'titlePhoto': 'https://userpic.codeforces.org/no-title.jpg'
    },
    {
        'avatar': 'https://userpic.codeforces.org/no-avatar.jpg',
        'contribution': 7,
        'country': 'India',
        'firstName': 'Rahul',
        'friendOfCount': 50,
        'handle': 'rahulcodes',
        'lastOnlineTimeSeconds': 1723190201,
        'maxRank': 'expert',
        'maxRating': 1800,
        'organization': 'IIT Delhi',
        'rank': 'expert',
        'rating': 1780,
        'registrationTimeSeconds': 1660933170,
        'titlePhoto': 'https://userpic.codeforces.org/no-title.jpg'
    }
    ]

    # print(sorted(users, key=lambda user: user['rating'], reverse=True))




