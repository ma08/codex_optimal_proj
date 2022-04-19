
import sys
import re

def main():
    # write your code here.
    # input comes from standard input.

    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = re.split('\\s+', line)
        # increase counters
        for word in words:
            # write the results to standard output;
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            print('%s\t%s' % (word, 1))

if __name__ == '__main__':
    main()
