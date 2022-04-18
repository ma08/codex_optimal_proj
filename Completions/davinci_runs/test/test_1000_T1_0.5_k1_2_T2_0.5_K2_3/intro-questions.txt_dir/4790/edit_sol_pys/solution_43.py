

import sys

def main():
    data = sys.stdin.read().splitlines()
    s = data[0].split()
    if len(s[0]) == 1:
        print(1)
        return
    b_count = 0
    w_count = 0
    for i in range(len(s[0])):
        if s[0][i] == 'B':
            b_count += 1
        else:
            w_count += 1
    if b_count == w_count:
        print(1)
        return
    if abs(b_count - w_count) == 1:
        print(1)
        return
    print(0)

if __name__ == "__main__":
    main()
