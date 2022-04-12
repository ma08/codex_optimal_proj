import os
import sys
import re
import shutil
import argparse
import logging
import subprocess
import configparser
import tempfile
import time
import datetime
import json
import requests
import xml.etree.ElementTree as ET


def get_args():
    parser = argparse.ArgumentParser(description='Script to get the file from the server')
    parser.add_argument('--file', help='File to get', required=True)
    parser.add_argument('--dest', help='Destination to save the file', required=True)
    parser.add_argument('--url', help='URL to get the file', required=True)
    args = parser.parse_args()
    return args


def get_file(file, dest, url):
    try:
        r = requests.get(url + file)
        with open(dest + file, 'wb') as f:
            f.write(r.content)
        return True
    except Exception as e:
        logging.error(e)
        return False


def main():
    args = get_args()
    file = args.file
    dest = args.dest
    url = args.url
    if get_file(file, dest, url):
        print("File downloaded")
    else:
        print("File not downloaded")



if __name__ == "__main__":
    main()
