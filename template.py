# -*- coding: utf-8 -*-

import json
import os
from sys import exit


class Template:
    """"Этот класс отвечает за работу с шаблонами"""
    def __init__(self, template):
        self.template = template

    def get_template(self):
        f = os.getcwd() + '/template.json'
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as f:
                try:
                    self.template = json.loads(f.read())
                    for key in self.template.keys():
                        if key not in self.template:
                            print('Не хватает параметров в шаблоне')
                            exit()
                except json.decoder.JSONDecodeError:
                    print('Не удалось загрузить шаблон')
        return self.template
