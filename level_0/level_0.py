#!/usr/bin/python3
""" this module contains a script to vote for id 355 1024 times """
import requests


for i in range(1024):
    my_data = {'id': 355, 'holdthedoor': 'Submit'}
    page = requests.post('http://158.69.76.135/level0.php', data=my_data)
