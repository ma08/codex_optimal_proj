

import os
import sys
import time
import random
import requests
import json
import urllib
from pprint import pprint
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.request import Request
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class File:
    def __init__(self):
        pass

    def write(self, file_name, data):
        with open(file_name, 'w') as file:
            file.write(data)

    def read(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def append(self, file_name, data):
        with open(file_name, 'a') as file:
            file.write(data)

    def download(self, url, file_name):
        urlretrieve(url, file_name)

    def save_as(self, file_name):
        pass

    def open(self, file_name):
        pass

    def delete(self, file_name):
        pass
