# -*- coding: utf-8 -*-
import re
import os


class File(object):
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, content):
        with open(self.path, 'w') as f:
            f.write(content)

    def get_or_create_file(self):
        if not os.path.exists(self.path):
            self.write('')

    def set_line(self, line, value):
        self.get_or_create_file()
        content = self.read()
        content = re.sub(r'^.*$', value, content, flags=re.MULTILINE)
        self.write(content)

    def get_line(self, line):
        self.get_or_create_file()
        content = self.read()
        return re.findall(r'^.*$', content, flags=re.MULTILINE)[line - 1]

    def append(self, content):
        self.get_or_create_file()
        content = self.read() + content
        self.write(content)


if __name__ == '__main__':
    f = File('./test')
    f.append('\n')
    f.append('hello')
    f.set_line(1, 'hello')
    print f.get_line(1)
