# -*- coding: utf-8 -*-
import os
import time

import requests

import db

bot_token = os.environ['bot_token']
channel_id = '@' + os.environ['channel_id']
bad = ['icon pack', 'substratum', 'porn']

def send_to_telegram(text):
    return requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(bot_token, 'sendMessage'),
        data={'chat_id': channel_id, 'text': text, 'parse_mode': 'HTML'}
    )


if __name__ == '__main__':

    query = {'ispub': False}
    published_query = {'$set': {'ispub': True}}
    for x in db.post_collection.find(query):
        json = x['json']
        title = json['subject']
        if any(x in title.lower() for x in bad):
            continue
        author = json['name']
        desc = json['preview']
        url = 'https://forum.mobilism.org' + json['browser_url']
        message = f'<a href="{url}">{title}</a>' \
                  f"\n\n" \
                  f'<pre>{desc}</pre>' \
                  f"\n\n" \
                  f'by: <pre>{author}</pre>'
        print(message)
        sent = send_to_telegram(message)
        print(sent)
        if sent.status_code == 200:
            db.post_collection.update_one({'pid': x['pid']}, published_query)
            time.sleep(3)
