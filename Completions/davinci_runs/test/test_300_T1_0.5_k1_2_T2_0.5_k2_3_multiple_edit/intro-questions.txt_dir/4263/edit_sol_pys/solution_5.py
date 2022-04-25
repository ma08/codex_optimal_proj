import sys

def main():
    S = sys.stdin.readline().rstrip()  # strip() removes the newline character at the end
    max_len = 0
    curr_len = 0
    for c in S:
        if c in ['A', 'C', 'G', 'T']:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 0
    if curr_len > max_len:
        max_len = curr_len
    print(max_len)

if __name__ == '__main__':  # execute only if run as a script
    main()
