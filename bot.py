# -*- coding: utf-8 -*-
import os

import requests

import db
import market_link
from post import Post

bot_token = os.environ['bot_token']
channel_id = os.environ['channel_id']


def send_to_telegram(args):
    text_caps = ''.join(args)
    return requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
        data={'chat_id': channel_id, 'text': text_caps, 'parse_mode': 'HTML'}
    ).json()


if __name__ == '__main__':

    query = {'ispub': False}
    published_query = {'$set': {'ispub': True}}
    for x in db.post_collection.find(query):
        market_url = market_link.get_link(x['link'])
        post = Post(x['title'], x['link'])
        if market_url is None:
            if send_to_telegram(post.get_message_html()).status_code == 200:
                db.post_collection.update_one({'link': x['link']}, published_query)
        else:
            if send_to_telegram(post.get_message_html_with_market_link(market_url)).status_code == 200:
                db.post_collection.update_one({'link': x['link']}, published_query)
