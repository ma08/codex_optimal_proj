

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_file_content(file_list):
    file_content = []
    for file in file_list:
        with open(file, 'r') as f:
            file_content.append(f.read())
    return file_content


def get_file_content_from_path(path):
    file_list = get_file_list(path)
    file_content = get_file_content(file_list)
    return file_content


def get_file_content_from_file(file):
    file_list = []
    file_list.append(file)
    file_content = get_file_content(file_list)
    return file_content


def get_file_content_from_stdin():
    file_content = []
    for line in sys.stdin:
        file_content.append(line)
    return file_content


def get_file_content_from_input(input):
    if input:
        if os.path.exists(input):
            if os.path.isfile(input):
                file_content = get_file_content_from_file(input)
            elif os.path.isdir(input):
                file_content = get_file_content_from_path(input)
            else:
                print('Unknown file type')
                sys.exit(1)
        else:
            print('File or path does not exist')
            sys.exit(1)
    else:
        file_content = get_file_content_from_stdin()
    return file_content


def get_args():
    args = {}
    args['input'] = ''
    args['output'] = ''
    args['pattern'] = ''
    args['ignore_case'] = False
    args['invert_match'] = False
    args['line_number'] = False
    args['count'] = False
    args['word_regexp'] = False
    args['line_regexp'] = False
    args['filename'] = False
    args['null'] = False
    args['help'] = False
    args['version'] = False
    args['debug'] = False
    return args


def parse_args():
    args = get_args()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == '-h' or arg == '--help':
                args['help'] = True
            elif arg == '-V' or arg == '--version':
                args['version'] = True
            elif arg == '-i' or arg == '--ignore-case':
                args['ignore_case'] = True
            elif arg == '-v' or arg == '--invert-match':
                args['invert_match'] = True
            elif arg == '-n' or arg == '--line-number':
                args['line_number'] = True
            elif arg == '-c' or arg == '--count':
                args['count'] = True
            elif arg == '-w' or arg == '--word-regexp':
                args['word_regexp'] = True
            elif arg == '-x' or arg == '--line-regexp':
                args['line_regexp'] = True
            elif arg == '-l' or arg == '--files-with-matches':
                args['filename'] = True
            elif arg == '-Z' or arg == '--null':
                args['null'] = True
            elif arg == '-d' or arg == '--debug':
                args['debug'] = True
            elif arg.startswith('-'):
                print('Unknown option: ' + arg)
                sys.exit(1)
            elif args['pattern'] == '':
                args['pattern'] = arg
            elif args['input'] == '':
                args['input'] = arg
            else:
                print('Unknown option: ' + arg)
                sys.exit(1)
    return args


def print_help():
    print('Usage:')
    print('  python3 file.py [OPTION]... PATTERN [FILE]...')
    print('  python3 file.py [OPTION]... -e PATTERN... [FILE]...')
    print('  python3 file.py [OPTION]... -f FILE [FILE]...')
    print('  python3 file.py [OPTION]... [-e PATTERN]... -f FILE [FILE]...')
    print('  python3 file.py [OPTION]... --files0-from=F [FILE]...')
    print('Search for PATTERN in each FILE or standard input.')
    print('PATTERN is, by default, a basic regular expression (BRE).')
    print('Example:')
    print('  python3 file.py -i -n -w -c -l -d --files0-from=F -e PATTERN -f FILE')
    print('  python3 file.py -i -n -w -c -l -d -e PATTERN -f FILE')
    print('  python3 file.py -i -n -w -c -l -d -e PATTERN FILE')
    print('  python3 file.py -i -n -w -c -l -d -e PATTERN')
    print('  python3 file.py -i -n -w -c -l -d FILE')
    print('  python3 file.py -i -n -w -c -l -d')


def print_version():
    print('file.py 1.0.0')


def print_file_content(file_content):
    for line in file_content:
        print(line)


def main():
    args = parse_args()
    if args['help']:
        print_help()
        sys.exit(0)
    elif args['version']:
        print_version()
        sys.exit(0)
    else:
        file_content = get_file_content_from_input(args['input'])
        print_file_content(file_content)


if __name__ == '__main__':
    main()
