#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
if __name__ == '__main__':
    import urllib.request
    import sys
    from urllib.error import URLError

    request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode(encoding='utf-8'))
    except URLError as error:
        print('Error code: {}'.format(error.getcode()))
