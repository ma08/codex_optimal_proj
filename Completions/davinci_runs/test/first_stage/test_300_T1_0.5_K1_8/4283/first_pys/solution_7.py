

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()

    # print(n, a)

    t = {}
    for i in a:
        if i not in t:
            t[i] = 1
        else:
            t[i] += 1
    # print(t)

    max_len = 0
    for key in t:
        cur_len = 0
        for i in range(-5, 6):
            if key + i in t:
                cur_len += t[key + i]
        # print(key, cur_len)
        if cur_len > max_len:
            max_len = cur_len

    print(max_len)


if __name__ == '__main__':
    main()