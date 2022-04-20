#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

def file_put_contents(filename, data):
    with open(filename, 'w') as f:
        return f.write(data)

def file_exists(filename):
    return os.path.isfile(filename)

def file_get_contents_utf8(filename):
    return file_get_contents(filename).decode('utf-8')

def file_put_contents_utf8(filename, data):
    return file_put_contents(filename, data.encode('utf-8'))

def file_get_contents_binary(filename):
    with open(filename, 'rb') as f:
        return f.read()

def file_put_contents_binary(filename, data):
    with open(filename, 'wb') as f:
        return f.write(data)

def file_put_contents_append(filename, data):
    with open(filename, 'a') as f:
        return f.write(data)

#def file_put_contents_append_utf8(filename, data):
#    return file_put_contents_append(filename, data.encode('utf-8'))

def file_put_contents_append_utf8(filename, data):
    with open(filename, 'a') as f:
        return f.write(data.encode('utf-8'))

def file_put_contents_append_binary(filename, data):
    with open(filename, 'ab') as f:
        return f.write(data)

def file_get_contents_from_url(url):
    import urllib2
    return urllib2.urlopen(url).read()

def file_get_contents_from_url_utf8(url):
    return file_get_contents_from_url(url).decode('utf-8')

def file_get_contents_from_url_binary(url):
    import urllib2
    return urllib2.urlopen(url).read()

def file_put_contents_from_url(url, data):
    import urllib2
    return urllib2.urlopen(url, data).read()

def file_put_contents_from_url_utf8(url, data):
    return file_put_contents_from_url(url, data.encode('utf-8')).decode('utf-8')

def file_put_contents_from_url_binary(url, data):
    return file_put_contents_from_url(url, data)

def file_get_contents_from_url_post(url, data):
    import urllib
    import urllib2
    postdata = urllib.urlencode(data)
    return urllib2.urlopen(url, postdata).read()

def file_get_contents_from_url_post_utf8(url, data):
    return file_get_contents_from_url_post(url, data).decode('utf-8')

def file_get_contents_from_url_post_binary(url, data):
    return file_get_contents_from_url_post(url, data)

def file_put_contents_from_url_post(url, data):
    import urllib
    import urllib2
    postdata = urllib.urlencode(data)
    return urllib2.urlopen(url, postdata).read()

def file_put_contents_from_url_post_utf8(url, data):
    return file_put_contents_from_url_post(url, data).decode('utf-8')

def file_put_contents_from_url_post_binary(url, data):
    return file_put_contents_from_url_post(url, data)

def file_put_contents_from_url_post_append(url, data):
    import urllib
    import urllib2
    postdata = urllib.urlencode(data)
    return urllib2.urlopen(url, postdata).read()

def file_put_contents_from_url_post_append_utf8(url, data):
    return file_put_contents_from_url_post_append(url, data).decode('utf-8')

def file_put_contents_from_url_post_append_binary(url, data):
    return file_put_contents_from_url_post_append(url, data)

def file_get_contents_from_url_post_append(url, data):
    import urllib
    import urllib2
    postdata = urllib.urlencode(data)
    return urllib2.urlopen(url, postdata).read()

def file_get_contents_from_url_post_append_utf8(url, data):
    return file_get_contents_from_url_post_append(url, data).decode('utf-8')

def file_get_contents_from_url_post_append_binary(url, data):
    return file_get_contents_from_url_post_append(url, data)
