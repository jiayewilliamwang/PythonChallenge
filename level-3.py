#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

num = "72758"

while num.isdigit():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    page = requests.get(url)
    num = str(soup).split()[-1]
    print(num)




