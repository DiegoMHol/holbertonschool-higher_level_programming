#!/usr/bin/python3
""" script that takes your Github credentials (username and password) """
if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/user'
    gith = {'login': sys.argv[1]}
    response = requests.get(url, params=gith, auth=(
        sys.argv[1], sys.argv[2])).json()

    try:
        print(response['id'])
    except KeyError:
        print('None')
