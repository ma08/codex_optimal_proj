#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]
    dic = {}
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = dic.keys()
    answer = 0
    for i, k1 in enumerate(keys):
        for j, k2 in enumerate(keys[i+1:]):
            for k, k3 in enumerate(keys[j+1:]):
                answer += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(answer)


if __name__ == '__main__':
    main()
