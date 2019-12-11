# -*- coding: utf-8 -*-

import crawler

import db

if __name__ == '__main__':

    fetched = crawler.parse()
    for p in fetched:
        query = {'link': p.link}
        if db.post_collection.count_documents(query) == 0:
            x = db.post_collection.insert_one(p.get_dic())
            print(x.inserted_id)
