#!/usr/bin/env python3



import logging
import os
import time
from datetime import datetime
from datetime import timedelta

import click
import click_log
import requests


logger = logging.getLogger(__name__)
click_log.basic_config(logger)


def get_cookies(session, username, password):
    """
    Get cookies from login form

    :param session: requests session
    :param username: username
    :param password: password
    :return: cookies
    """
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_data = {
        'username': username,
        'password': password,
    }
    session.post(login_url, data=login_data)
    return session.cookies


def get_media_urls(session, user_id):
    """
    Get media URLs from user ID

    :param session: requests session
    :param user_id: user ID
    :return: media URLs
    """
    media_url = 'https://www.instagram.com/graphql/query/'
    media_params = {
        'query_hash': 'f2405b236d85e8296cf30347c9f08c2a',
        'variables': '{"id":"{}","first":50}'.format(user_id),
    }
    media_response = session.get(media_url, params=media_params)
    media_json = media_response.json()
    media_urls = []
    for edge in media_json['data']['user']['edge_owner_to_timeline_media']['edges']:
        media_urls.append(edge['node']['display_url'])
    return media_urls


def get_user_id(session, username):
    """
    Get user ID from username

    :param session: requests session
    :param username: username
    :return: user ID
    """
    user_url = 'https://www.instagram.com/{}/'.format(username)
    user_response = session.get(user_url)
    user_id = user_response.text.split('"id":"')[1].split('"')[0]
    return user_id


def download_media(session, media_urls, filename, sleep):
    """
    Download media from list of URLs

    :param session: requests session
    :param media_urls: list of media URLs
    :param filename: filename
    :param sleep: sleep time
    """
    with open(filename, 'w') as file:
        for media_url in media_urls:
            media_response = session.get(media_url)
            file.write(media_response.content)
            time.sleep(sleep)


def get_media(username, password, sleep=1):
    """
    Get media from username

    :param username: username
    :param password: password
    :param sleep: sleep time
    """
    session = requests.Session()
    session.cookies = get_cookies(session, username, password)
    user_id = get_user_id(session, username)
    media_urls = get_media_urls(session, user_id)
    download_media(session, media_urls, 'media.jpg', sleep)


@click.command()
@click.option('--username', '-u', required=True, type=str, help='Username')
@click.option('--password', '-p', required=True, type=str, help='Password')
@click.option('--sleep', '-s', default=1, type=int, help='Sleep time')
@click.option('--loglevel', '-l', default='INFO', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
              help='Log level')
@click_log.simple_verbosity_option(logger)
def cli(username, password, sleep, loglevel):
    """
    Get media from username

    :param username: username
    :param password: password
    :param sleep: sleep time
    :param loglevel: log level
    """
    logging.getLogger().setLevel(loglevel)
    get_media(username, password, sleep)



def main():
    cli()




if __name__ == '__main__':
    main()
