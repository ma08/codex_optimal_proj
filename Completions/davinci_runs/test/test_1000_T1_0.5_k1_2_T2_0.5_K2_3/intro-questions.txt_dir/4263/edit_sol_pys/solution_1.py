import sys

def main():
    S = sys.stdin.readline().strip()
    max_len = 0
    curr_len = 1
    for c in S:
        if c == 'A' or c == 'C' or c == 'G' or c == 'T':
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
    if curr_len > max_len:
        max_len = curr_len
    print(max_len)

if __name__ == '__main__':
    main()
