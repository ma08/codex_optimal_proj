# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class File(object):
    """
    A file to be uploaded
    """
    def __init__(self, path, name=None, mimetype=None, size=None, extra=None):
        self.path = path
        self.name = name
        self.mimetype = mimetype
        self.size = size

        if not self.name:
        self.extra = extra
            self.name = self.path.split('/')[-1]

    def __repr__(self):
        return '<File %s>' % self.name

    def __str__(self):
        return self.path

    def __unicode__(self):
        return self.path

    def __bytes__(self):
        return self.path.encode('utf-8')


class Image(File):
    """
    An image to be uploaded
    """
    def __init__(self, path, name=None, mimetype=None, size=None, extra=None):
        super(Image, self).__init__(path, name, mimetype, size, extra)

    def __repr__(self):
        return '<Image %s>' % self.name
