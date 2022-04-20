

import sys
import os
import shutil
import time
import datetime
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Move files to archive')
    parser.add_argument('--dir', help='Directory to move files from', required=True)
    parser.add_argument('--archive', help='Directory to move files to', required=True)
    parser.add_argument('--days', help='Days to keep files', required=True)
    return parser.parse_args()

def get_files(dir, days):
    files = []
    for filename in os.listdir(dir):
        full_path = os.path.join(dir, filename)
        if os.path.isfile(full_path):
            file_time = os.path.getmtime(full_path)
            if (time.time() - file_time) // (24 * 3600) > days:
                files.append(full_path)
    return files

def move_files(files, archive):
    for file in files:
        shutil.move(file, archive)

def main(dir, archive, days):
    files = get_files(dir, days)
    move_files(files, archive)

if __name__ == "__main__":
    args = parse_args()
    main(args.dir, args.archive, int(args.days))
