#!/usr/bin/python

import sys
import os
import re

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            infile = open(filename, 'r')
            content = infile.read()
            infile.close()

            outfile = open(filename, 'w')
            outfile.write(re.sub(r"\b(a|A)n (\w+)", r"\1 \2", content)) # re.sub(pattern, repl, string)
            outfile.close()

if __name__ == '__main__':
    main()
