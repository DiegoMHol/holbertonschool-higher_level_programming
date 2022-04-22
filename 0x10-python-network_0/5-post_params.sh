#!/bin/bash
# takes in a URL and displays all HTTP methods
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
