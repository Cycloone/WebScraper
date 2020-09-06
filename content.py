# -*- coding: utf-8 -*-

class Content:
    """"Этот класс отвечает за финальную обработку данных"""
    def __init__(self, template, content):
        self.template = template
        self.content = content

    def format_data(self):
        current_template = self.template
        unformatted = self.content
        text = ''
        rows = []
        while unformatted:
            if len(unformatted) <= current_template['rows_length']:
                rows.append(unformatted)
                unformatted = ''
            else:
                line_break = unformatted.find('\n\n')
                if line_break < current_template['rows_length'] and line_break != -1:
                    rows.append(unformatted[:line_break] + '\n')
                    unformatted = unformatted[line_break + 2:]
                else:
                    for i in range(current_template['rows_length'] + 1, 0, -1):
                        if str.isspace(unformatted[i]):
                            rows.append(unformatted[:i])
                            unformatted = unformatted[i + 1:]
                            break
        for s in rows:
            text = '%s%s\n' % (text, s)
        return text
