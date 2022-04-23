#!/usr/bin/python3
""" Take a URL and a EMAIL, display body of response """
if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    email = urllib.parse.urlencode({'email': sys.argv[2]})
    email = email.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode(encoding='utf-8'))
