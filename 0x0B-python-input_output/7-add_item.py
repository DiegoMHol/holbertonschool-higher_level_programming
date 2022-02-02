#!/usr/bin/python3
""" Add arg save """
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_list = []
try:
    my_load = load_from_json_file('add_item.json')
    for i in my_load:
        my_list.append(i)
Exception:
    my_list = []
for j in range(1, len(argv)):
    my_list.append(argv[j])
save_to_json_file(my_list, 'add_item.json')
