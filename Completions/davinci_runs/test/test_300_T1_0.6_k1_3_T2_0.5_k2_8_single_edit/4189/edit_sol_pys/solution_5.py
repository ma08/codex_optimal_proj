#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:knktc
@contact:me@knktc.com
@create:2018-06-06 11:08
"""

import os
import sys

from .server import Server
from .command import Command
from .utils import get_logger


def main():
    logger = get_logger()
    logger.info('start')
    logger.info('pid: {}'.format(os.getpid()))
    logger.info('uid: {}'.format(os.getuid()))
    logger.info('gid: {}'.format(os.getgid()))
    logger.info('cwd: {}'.format(os.getcwd()))
    logger.info('args: {}'.format(sys.argv))
    logger.info('env: {}'.format(os.environ.get('ENV')))
    logger.info('end')


if __name__ == '__main__':
    main()
