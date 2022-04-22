#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
import logging
import argparse
import tempfile
from contextlib import contextmanager

import pyinotify
from watchdog.observers import Observer
from watchdog.events import (FileCreatedEvent,
                             FileDeletedEvent,
                             FileModifiedEvent,
                             FileMovedEvent,
                             DirCreatedEvent,
                             DirDeletedEvent,
                             DirModifiedEvent,
                             DirMovedEvent,
                             PatternMatchingEventHandler)

logger = logging.getLogger(__name__)


class FileWatcher(PatternMatchingEventHandler):
    def __init__(self, patterns=None, ignore_patterns=None,
                 ignore_directories=False, case_sensitive=False):
        super(FileWatcher, self).__init__(
            patterns=patterns, ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories, case_sensitive=case_sensitive)

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            logger.info("File created: %s", event.src_path)
        elif isinstance(event, DirCreatedEvent):
            logger.info("Dir created: %s", event.src_path)

    def on_deleted(self, event):
        if isinstance(event, FileDeletedEvent):
            logger.info("File deleted: %s", event.src_path)
        elif isinstance(event, DirDeletedEvent):
            logger.info("Dir deleted: %s", event.src_path)

    def on_modified(self, event):
        if isinstance(event, FileModifiedEvent):
            logger.info("File modified: %s", event.src_path)
        elif isinstance(event, DirModifiedEvent):
            logger.info("Dir modified: %s", event.src_path)

    def on_moved(self, event):
        if isinstance(event, FileMovedEvent):
            logger.info("File moved: %s -> %s", event.src_path, event.dest_path)
        elif isinstance(event, DirMovedEvent):
            logger.info("Dir moved: %s -> %s", event.src_path, event.dest_path)


class InotifyWatcher(pyinotify.ProcessEvent):
    def __init__(self, mask, output_dir):
        super(InotifyWatcher, self).__init__()
        self.mask = mask
        self.output_dir = output_dir

    def process_IN_CREATE(self, event):
        logger.info("File created: %s", event.pathname)

    def process_IN_DELETE(self, event):
        logger.info("File deleted: %s", event.pathname)

    def process_IN_MODIFY(self, event):
        logger.info("File modified: %s", event.pathname)

    def process_IN_MOVED_FROM(self, event):
        logger.info("File moved from: %s", event.pathname)

    def process_IN_MOVED_TO(self, event):
        logger.info("File moved to: %s", event.pathname)


@contextmanager
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def main(args):
    logger.info("Started: %s", args)

    watch_dir = args.watch_dir
    patterns = args.patterns
    ignore_patterns = args.ignore_patterns
    ignore_directories = args.ignore_directories
    case_sensitive = args.case_sensitive
    recursive = args.recursive
    inotify = args.inotify
    polling_interval = args.polling_interval

    if inotify:
        wm = pyinotify.WatchManager()
        notifier = pyinotify.Notifier(wm, InotifyWatcher(
            pyinotify.ALL_EVENTS, args.output_dir))
        wm.add_watch(watch_dir, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    else:
        event_handler = FileWatcher(
            patterns=patterns,
            ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories,
            case_sensitive=case_sensitive)
        observer = Observer()
        observer.schedule(event_handler, watch_dir, recursive=recursive)
        observer.start()

    try:
        while True:
            if inotify:
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            else:
                time.sleep(polling_interval)
    except KeyboardInterrupt:
        pass
    finally:
        if inotify:
            notifier.stop()
        else:
            observer.stop()
            observer.join()

    logger.info("Finished: %s", args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('watch_dir', help='Directory to be watched')
    parser.add_argument('-p', '--patterns', nargs='+', default=['*'],
                        help='List of filename patterns to watch')
    parser.add_argument('-i', '--ignore-patterns', nargs='+', default=[],
                        help='List of filename patterns to ignore')
    parser.add_argument('-d', '--ignore-directories', action='store_true',
                        help='Ignores all directories')
    parser.add_argument('-c', '--case-sensitive', action='store_true',
                        help='Case sensitive pattern matching')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Watch directories recursively')
    parser.add_argument('--inotify', action='store_true',
                        help='Use inotify')
    parser.add_argument('--polling-interval', type=float, default=1.0,
                        help='Polling interval (sec)')
    parser.add_argument('--output-dir', default='.',
                        help='Output directory')
    args = parser.parse_args()

    main(args)
