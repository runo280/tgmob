# -*- coding: utf-8 -*-
import os

import requests

import db

bot_token = os.environ['bot_token']
channel_id = os.environ['channel_id']


def send_to_telegram(args):
    text_caps = ''.join(args)
    return requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
        data={'chat_id': channel_id, 'text': text_caps, 'parse_mode': 'HTML'}
    )


if __name__ == '__main__':

    query = {'ispub': False}
    published_query = {'$set': {'ispub': True}}
    for x in db.post_collection.find(query):
        json = x['json']
        title = json['subject']
        author = json['name']
        desc = json['preview']
        url = 'https://forum.mobilism.org' + json['browser_url']
        message = f'<a href={url}>{title}</a><br><br><pre>{desc}</pre><br><br>by: <pre>{author}</pre>'
        if send_to_telegram(message).status_code == 200:
            db.post_collection.update_one({'pid': x['pid']}, published_query)
