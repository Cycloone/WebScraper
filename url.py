# -*- coding: utf-8 -*-

import urllib
from urllib.parse import urlparse
import requests


class Url:
    """"Этот класс отвечает за работу с url"""

    def __init__(self, url):
        self.url = url

    def get_content(self):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}
            dry_data = requests.get(self.url, headers=headers)
            return dry_data.text
        except requests.exceptions.InvalidSchema:
            print('Проверьте свой URL. Неправильная ссылка.')

    def parse_url(self):
        url_to_path = urllib.parse.urlparse(self.url)
        url_str = '%s%s' % (url_to_path[1], url_to_path[2])
        return url_str
