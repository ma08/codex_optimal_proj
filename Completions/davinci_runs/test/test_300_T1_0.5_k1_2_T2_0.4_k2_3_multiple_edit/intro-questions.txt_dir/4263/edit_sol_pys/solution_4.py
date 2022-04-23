

import sys


def main():
    S = sys.stdin.readline().rstrip()  # strip() removes \n
    max_len = 0
    curr_len = 0
    for c in S:  # iterate over the string
        if c == 'A' or c == 'C' or c == 'G' or c == 'T':  # if c is a nucleotide
            curr_len += 1
        else:  # if c is not a nucleotide
            if curr_len > max_len:  # if the current sequence is the longest
                max_len = curr_len
            curr_len = 0  # reset current sequence length
    if curr_len > max_len:  # if the last sequence is the longest
        max_len = curr_len
    print(max_len)  # print the longest sequence length

if __name__ == '__main__':
    main()
