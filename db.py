# -*- coding: utf-8 -*-
import os
import pymongo

db_url = 'mongodb://{user}:{pwd}@{murl}/?ssl=true&replicaSet=Main0-shard-0&authSource=admin&retryWrites=true&w=majority'
db_user = os.environ['muser']
db_pass = os.environ['mpass']
db_domain = os.environ['murl']
db_name = 'mobilism'
db_posts = 'posts'
db_url = db_url.format(user=db_user, pwd=db_pass, murl=db_domain)
client = pymongo.MongoClient(db_url)
database = client[db_name]
post_collection = database['posts']


def add_to_db(post_list):
    for post in post_list:
        query = {'pid': post.pid}
        if post_collection.count_documents(query) == 0:
            x = post_collection.insert_one(post.get_dic())
            print(x.inserted_id)
