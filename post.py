# -*- coding: utf-8 -*-
class Post:
    def __init__(self, title, link, is_published=False):
        self.title = title
        self.link = link
        self.is_published = is_published

    def get_message(self):
        return "[{title}]({link})".format(title=self.title, link=self.link)

    def get_message_html(self):
        return "<a href=\"{link}\">{title}</a>".format(title=self.title, link=self.link)

    def get_message_html_with_market_link(self, market):
        return "{market}\n\n<a href=\"{link}\">{title}</a>".format(market=market, title=self.title, link=self.link)

    def get_dic(self):
        return {'title': self.title, 'link': self.link, 'ispub': False}
