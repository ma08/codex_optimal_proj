#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import time
import json
import logging
import traceback
import random
import string
import base64
import uuid
import hashlib
import urllib
import urllib.parse
import urllib.request
import urllib.error
import urllib.request
import urllib.parse
import urllib.error
import http.client
import socket
import ssl
import re
import zlib
import gzip
import shutil
import binascii
import mimetypes
import tempfile
import datetime
import threading
import queue
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import pprint
import argparse

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

pp = pprint.PrettyPrinter(indent=4)

def get_arguments():
    parser = argparse.ArgumentParser(description='', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--title', type=str, help='', required=True)
    parser.add_argument('-b', '--body', type=str, help='', default='')
    parser.add_argument('-f', '--file', type=str, help='', default='')
    parser.add_argument('-r', '--recipient', type=str, help='', default='', required=True)
    args = parser.parse_args()
    return args

def send_mail(title, body, recipient):
    sender = 'sender@domain.com'
    subject = title
    smtpserver = 'smtp.domain.com'
    username = 'user'
    password = 'password'

def get_min_days(cups, m):
    if get_pages_written_for_n_days(cups, 1) >= m:
        return 1
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if get_pages_written_for_n_days(cups, mid) >= m:
            right = mid
        else:
            left = mid + 1
    if get_pages_written_for_n_days(cups, left) >= m:
        return left
    else:
        return -1

print(get_min_days(cups, m))
