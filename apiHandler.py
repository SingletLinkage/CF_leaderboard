import hashlib
import time
import random
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def generate_codeforces_api_signature(api_key, secret, method_name, params):
    # Generate current Unix time
    unix_time = int(time.time())
    
    # Generate a random 6-character prefix
    rand = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    
    # Add the required parameters to the params dictionary
    params['apiKey'] = api_key
    params['time'] = str(unix_time)
    
    # Sort the parameters lexicographically first by key, then by value
    sorted_params = sorted(params.items())
    
    # Create the string to be hashed
    param_str = '&'.join(f'{k}={v}' for k, v in sorted_params)
    signature_base_string = f"{rand}/{method_name}?{param_str}#{secret}"
    
    # Generate the SHA-512 hash
    hash_value = hashlib.sha512(signature_base_string.encode('utf-8')).hexdigest()
    
    # Create the full apiSig
    api_sig = rand + hash_value
    
    return api_sig, unix_time


def get_url_using_auth(method_name, params):

    api_key = os.getenv('apiKey')
    secret = os.getenv('secret')

    api_sig, unix_time = generate_codeforces_api_signature(api_key, secret, method_name, params)


    # Construct the final request URL
    base_url = f"https://codeforces.com/api/{method_name}"
    param_url = '&'.join([f'{k}={v}' for k,v in params.items()])
    request_url = f"{base_url}?{param_url}&apiSig={api_sig}"

    return request_url

def api_custom_call(url):
    try:
        _ = requests.get(url).text
        response = json.loads(_)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(_)
        return
    
    if response['status'] != 'OK':
        print(response['comment'])
    else:
        return response['result']

if __name__ == '__main__':
    handles = ['qchaos', 'CrazyWarlord', 'HemckerOO7']
    method_name = 'user.info'
    params = {
        'handles': ';'.join(handles)
    }

    print(params)

    url = get_url_using_auth(method_name=method_name, params=params)
    response = api_custom_call(url=url)
    # users = sorted(response, key=lambda user: user['rating'], reverse=True)
    print(url, response)