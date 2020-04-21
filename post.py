# -*- coding: utf-8 -*-
class Post:
    def __init__(self, pid, json, is_published=False):
        self.pid = pid
        self.json = json
        self.is_published = is_published

    def get_dic(self):
        return {'pid': self.pid, 'json': self.json, 'ispub': False}
