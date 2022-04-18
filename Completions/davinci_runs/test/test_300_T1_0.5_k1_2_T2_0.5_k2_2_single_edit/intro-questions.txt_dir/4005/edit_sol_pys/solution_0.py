#!/usr/bin/env python3
import argparse
import os
import shutil
import sys
import filecmp

parser = argparse.ArgumentParser(description='Copy files to a new location. If the file already exists, prompt the user to overwrite it')
parser.add_argument('source', help='The file or directory to be copied')
parser.add_argument('destination', help='The destination file or directory')
parser.add_argument('-f', '--force', help='Overwrite the destination file or directory if it already exists', action='store_true')
args = parser.parse_args()

if not os.path.exists(args.source):
    print(f'{args.source} does not exist')
    sys.exit(1)

if os.path.exists(args.destination):
    if args.force:
        shutil.rmtree(args.destination)
    else:
        if os.path.isdir(args.destination):
            if filecmp.dircmp(args.source, args.destination).same_files:
                print(f'{args.source} and {args.destination} are identical')
                sys.exit(0)
            else:
                prompt = f'{args.destination} already exists. Overwrite? [y/n]: '
                response = input(prompt)
                if response.lower() == 'y':
                    shutil.rmtree(args.destination)
                else:
                    print('Exiting')
                    sys.exit(0)
        else:
            prompt = f'{args.destination} already exists. Overwrite? [y/n]: '
            response = input(prompt)
            if response.lower() == 'y':
                os.remove(args.destination)
            else:
                print('Exiting')
                sys.exit(0)

if os.path.isdir(args.source):
    shutil.copytree(args.source, args.destination)
else:
    shutil.copy(args.source, args.destination)
