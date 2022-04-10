

import sys

def main():
    data = sys.stdin.read().splitlines()
    s = data[0]
    if len(s) == 1:
        print(1)
        return
    b_count = 0
    w_count = 0
    for i in range(len(s)):
        if s[i] == 'B':
            b_count += 1
        else:
            w_count += 1
    if b_count == w_count:
        print(1)
        return
    if b_count > w_count:
        if b_count - w_count == 1:
            print(1)
            return
    if w_count > b_count:
        if w_count - b_count == 1:
            print(1)
            return
    print(0)

if __name__ == "__main__":
    main()