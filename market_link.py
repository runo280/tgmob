# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_link(url):
    page = requests.get(url)
    if page.status_code != 200:
        print('Failed to get page')
        return None

    soap = BeautifulSoup(page.text, 'html.parser')
    code = soap.find('code')
    if code is not None:
        return code.text
    else:
        print('Link not found')
        return None
