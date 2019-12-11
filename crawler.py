# -*- coding: utf-8 -*-
import hashlib
import os

import requests
from bs4 import BeautifulSoup

from post import Post

baseUrl = os.environ['moburl']


def get_md5(arg):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()


def parse():
    post_list = []
    page = requests.get(baseUrl)
    if page.status_code == 200:
        soap = BeautifulSoup(page.text, 'html.parser')
        main = soap.find('main', {'role': 'main'})
        table = main.findAll('table')[1]
        thread = table.find('tbody')
        posts = thread.findAll('tr')
        for new in posts:
            if 'sticky' not in new['class']:
                if any(ext in new.find('small').text for ext in ['Today', 'Yesterday', 'minutes']):
                    link = new.find('a')
                    title = link.text
                    url = os.environ['moburl_base'] + link['href'][1:]
                    url = url[:url.rfind('&')]
                    new_post = Post(title, url)
                    post_list.append(new_post)
    else:
        print('error')
    return post_list
