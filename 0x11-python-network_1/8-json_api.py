#!/usr/bin/python3
""" script that takes in a letter and sends a POST """
if __name__ == '__main__':
    import sys
    import requests

    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]
    letter = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=letter).json()
        if response:
            print('[{}] {}'.format(response['id'], response['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
