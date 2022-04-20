from __future__ import print_function

import os
import sys
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def log(s):
    print('[Monitor] %s' % s)

class MyFileSystemEventHandler(PatternMatchingEventHandler):
    patterns = ["*.py", "*.html", "*.css"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for degug

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyFileSystemEventHandler(), path=args[0] if args else '.')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
