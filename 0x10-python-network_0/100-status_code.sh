#!/bin/bash
# sends a DELETE request to the URL
curl -s -o /dev/null -w "%{http_code}" "$1"
