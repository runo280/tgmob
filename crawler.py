# -*- coding: utf-8 -*-
import os

import requests

import db
from post import Post

baseUrl = os.environ['base_url']


def get_post_list():
    post_list = []
    for i in range(1, 5):
        new = baseUrl + f"page/{i}/limit/10/orderby/date/desc/0"
        page = requests.get(new)
        if page.status_code == 200:
            apps = page.json()['response']
            for post in apps:
                new_post = Post(post['id'], post)
                post_list.append(new_post)
    return post_list


if __name__ == '__main__':
    fetched = get_post_list()
    db.add_to_db(fetched)
