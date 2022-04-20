#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

class File(object):

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(self.path)
        self.size = os.path.getsize(self.path)
        self.ext = os.path.splitext(self.path)[1]
        self.mime = None
        self.content = None

    def get_mime(self):
        if self.size > 0:
            with open(self.path, "rb") as f:
                self.content = f.read()
                self.mime = magic.from_buffer(self.content, mime=True)

    def get_content(self):
        if self.size > 0:
            with open(self.path, "rb") as f:
                self.content = f.read()

    def __repr__(self):
        return "<File %s>" % (self.path)

    def __str__(self):
        return self.path
