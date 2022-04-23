#!/usr/bin/python3
""" Take a URL, display the value """
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
