
import sys


def main():
    S = sys.stdin.readline().rstrip()  # S = input()
    max_len = 0
    curr_len = 0
    for c in S:
        if c == 'A' or c == 'C' or c == 'G' or c == 'T':
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 0
    if curr_len > max_len:
        max_len = curr_len
    print(max_len)  # print(max_len, end='')


if __name__ == '__main__':
    main()
