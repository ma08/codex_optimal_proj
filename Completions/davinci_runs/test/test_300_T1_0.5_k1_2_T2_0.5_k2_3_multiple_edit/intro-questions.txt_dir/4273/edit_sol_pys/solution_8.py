#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]
    dic = dict()
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = dic.keys()
    answer = 0
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            for k in range(j+1, len(keys)):
                answer += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(answer)


if __name__ == '__main__':
    main()
