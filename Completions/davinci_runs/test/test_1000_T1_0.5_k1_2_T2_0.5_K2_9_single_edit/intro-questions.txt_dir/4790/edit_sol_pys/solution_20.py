

import sys

def main():
    data = sys.stdin.read().splitlines()
    s = data[0]
    b_count = 0
    w_count = 0
    for i in range(len(s)):
        if s[i] == 'B':
            b_count += 1
        else:
            w_count += 1
    if b_count == w_count or abs(b_count - w_count) == 1:
        print('1')
    else:
        print('0')

if __name__ == "__main__":
    main()
