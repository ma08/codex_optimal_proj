#!/usr/bin/env python3

import argparse
import logging

import time

def parse_args(args):
    parser = argparse.ArgumentParser(description='A simple word-counting utility.')
    parser.add_argument('-v', '--verbose', action='count', help='increase output verbosity')
    parser.add_argument('-l', '--log', metavar='FILE', type=argparse.FileType('a'), help='log to FILE')
    parser.add_argument('-n', '--num-words', type=int, default=10, help='the number of words to print')
    parser.add_argument('-r', '--reverse', action='store_true', help='reverse the output')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    return parser.parse_args(args)

def count_words(args):
    words = {}
    for f in args.files:
        for line in f:
            for word in line.split():
                words[word] = words.get(word, 0) + 1
    return words

def print_top_words(words, args):
    if args.reverse:
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    else:
        words = sorted(words.items(), key=lambda x: x[0])
    for word, count in words[:args.num_words]:
        print('{}: {}'.format(word, count))

def setup_logging(args):
    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose == 2:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    if args.log:
        handler = logging.FileHandler(args.log.name)
        handler.setLevel(logging.DEBUG)
        logging.getLogger().addHandler(handler)
import sys

def main():
    args = parse_args(sys.argv[1:])
    setup_logging(args)
    if not args.files:
        args.files = [sys.stdin]
    start_time = time.time()
    words = count_words(args)
    logging.info('Counting words took {:.2f} seconds'.format(time.time() - start_time))
    print_top_words(words, args)

if __name__ == '__main__':
    main()
