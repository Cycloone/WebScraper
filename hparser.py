# -*- coding: utf-8 -*-

from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    """"Этот класс отвечает за парсинг html"""
    def __init__(self, template):
        super().__init__()
        self.template = template
        self.content = ''
        self.record_flag = 0
        self.exclude_flag = 0
        self.paragraph_flag = 0
        self.url_flag = 0
        self.url_to_write = ''
        self.title_flag = 0
        self.nested_flag = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.template['exclude_tags']:
            self.exclude_flag = 1
            return

        if tag in self.template['nested_tags']:
            self.nested_flag = 1
        else:
            self.nested_flag = 0

        if tag in self.template['title_tags']:
            self.title_flag = 1

        if tag in self.template['content_tags']:
            self.record_flag = 1

        if tag == 'a' and self.record_flag and self.nested_flag:
            self.url_flag = 1
            self.url_to_write = attrs[0][1]
            self.url_to_write = '%s' % self.url_to_write
        else:
            return

    def handle_data(self, data):
        if len(data) == 0:
            return

        if self.exclude_flag:
            return

        if self.title_flag:
            self.content = '%s%s%s' % (self.content, data, '\n\n')
            self.title_flag = 0

        if self.record_flag:
            if self.paragraph_flag:
                self.content = '%s%s%s' % (self.content, '\n\n', data)
                self.paragraph_flag = 0

            if self.nested_flag:
                self.content = '%s%s' % (self.content, data)
                self.nested_flag = 0
            else:
                self.content = '%s%s' % (self.content, data)

            if self.url_flag:
                self.content = '%s [%s]' % (self.content, self.url_to_write)
                self.url_flag = 0

    def handle_endtag(self, tag):
        if tag in self.template['exclude_tags'] and self.exclude_flag:
            self.exclude_flag = 0
            return

        if tag in self.template['nested_tags'] and self.nested_flag:
            self.nested_flag = 0
            return

        if tag == self.template['content_tags'] and self.record_flag:
            self.record_flag = 0
            self.paragraph_flag = 1
