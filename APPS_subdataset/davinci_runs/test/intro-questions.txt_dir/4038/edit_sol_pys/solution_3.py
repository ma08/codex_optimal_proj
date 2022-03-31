#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import logging
import argparse

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path
        self.logger = logging.getLogger(__name__)

    def on_created(self, event):
        self.logger.info('created: %s' % event.src_path if event.is_directory else event.dest_path)

    def on_deleted(self, event):
        self.logger.info('deleted: %s' % event.src_path if event.is_directory else event.dest_path)

    def on_modified(self, event):
        self.logger.info('modified: %s' % event.src_path)
        self.logger.info('modified: %s' % event.dest_path)

    def on_moved(self, event):
        self.logger.info('moved: %s' % event.src_path if event.is_directory else event.dest_path)


def main():
    parser = argparse.ArgumentParser(description='Watchdog')
    parser.add_argument('--path', type=str, default=os.getcwd(),
                        help='path to watch')
    parser.add_argument('--log', type=str, default='log.txt',
                        help='log file')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=args.log,
                        filemode='w')

    event_handler = MyHandler(args.path)
    observer = Observer()
    observer.schedule(event_handler, args.path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
