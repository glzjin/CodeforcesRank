import random
import string
import urllib.parse

import requests


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def api_request(api, data):
    # api_data = {'apiKey': config.Config.key, 'handle': config.Config.username,
    #             'lang': 'en', 'time': int(time.time())}
    #
    # data.update(api_data)
    #
    # rand_str = random_word(6)
    #
    # final_keys = sorted(data.keys())
    # final_dict = {}
    # for key in final_keys:
    #     final_dict[key] = data[key]
    #
    # encrypt_str = rand_str + "/" + api + "?" + urllib.parse.urlencode(final_dict) + "#" + config.Config.secret
    #
    # hash_str = hashlib.sha512(encrypt_str.encode()).hexdigest()
    #
    # data['apiSig'] = rand_str + hash_str

    response = requests.get("https://codeforces.com/api/" + api + "?" + urllib.parse.urlencode(data))
    return response.json()
