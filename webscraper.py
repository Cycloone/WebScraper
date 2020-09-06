# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
import template
import url
import content
from hparser import MyHTMLParser


class WebScraper:
    """"Точка входа в программу"""

    def __init__(self):
        self.template = template.Template(template)
        arg_parser = ArgumentParser()
        arg_parser.add_argument("-u", "--url", dest="url")
        args = arg_parser.parse_args()
        if args.url is None:
            print("Вы забыли ввести URL")
        else:
            page = url.Url(args.url)
            data = page.get_content()
            path = page.parse_url()
            current_template = self.template.get_template()
            html_parser = MyHTMLParser(current_template)
            html_parser.feed(data)
            self.content = content.Content(current_template, html_parser.content)
            write_data = self.content.format_data()
            self.save_data(path, write_data)

    @staticmethod
    def save_data(path, data):
        path = path.replace('/', '\\')
        split_path = os.path.split(path)
        if len(split_path[1]) == 0:
            path = '%s%s' % (split_path[0], '.txt')
        else:
            path = '%s%s%s' % (split_path[0], split_path[1].split('.')[0], '.txt')
        file_path = os.getcwd() + '\\' + path
        dir_name = os.path.dirname(file_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(data)


if __name__ == '__main__':
    main = WebScraper()

