# coding: utf-8

import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)] # read all lines
    dic = {} # dictionary
    for name in names:
        if name[0] in dic: # first letter already exists
            dic[name[0]] += 1 # increment by 1
        else:
            dic[name[0]] = 1 # first time that letter appears
    keys = dic.keys() # list of keys
    ans = 0
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            for k in range(j+1, len(keys)):
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(ans)


if __name__ == '__main__':
    main()
