#!/usr/bin/python3
""" Take a URL, display the value of X-Request-Id """
if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
