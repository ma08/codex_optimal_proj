#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class File(object):
    def __init__(self, path):
        self.path = path

    def read(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return f.read()
        else:
            raise FileNotFoundError('file not found')

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def append(self, content):
        with open(self.path, 'a') as f:
            return f.write(content)

    def remove(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        else:
            raise FileNotFoundError('file not found')

    def copy(self, dst):
        if os.path.exists(self.path):
            with open(self.path) as rf:
                with open(dst, 'w') as wf:
                    for line in rf:
                        wf.write(line)
        else:
            raise FileNotFoundError('file not found')


if __name__ == '__main__':
    file = File('/tmp/test.txt')
    file.write('hello world')
    file.append('\nhello world')
    print(file.read())
    file.copy('/tmp/test2.txt')
    file.remove()
