#!/usr/bin/python3
"""
this module contains a script to vote for id 355 4096 times
on a website that only accepts votes from windows users and has a captcha
"""
import requests
import pytesseract
from PIL import Image


def get_captcha(cookies):
    cap = requests.get('http://54.221.6.249/captcha.php',
        cookies=cookies)
    with open(cap) as f:
        pic = Image.open(f)
    return pytesseract.image_to_string(pic)


url = 'http://158.69.76.135/level3.php'
page = requests.get(url)
fake_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0)\
Gecko/20100101 Firefox/50.0'
h = {'User-Agent': fake_windows, 'Referer': url}
cookies = page.cookies
pw = page.cookies['HoldTheDoor']
txt = {}
d = {'id': '10', 'holdthedoor': 'Submit', 'key': pw, 'captcha': txt}
for i in range(5):
    txt = get_captcha(cookies)
    res = requests.post(url, data=d, cookies={"HoldTheDoor": pw}, headers=h)
