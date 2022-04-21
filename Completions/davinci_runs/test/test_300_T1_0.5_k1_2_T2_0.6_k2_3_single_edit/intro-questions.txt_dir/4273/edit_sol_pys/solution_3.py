import os
import sys

import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]
    ans = 0
    dic = dict()
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
        for j in range(i+1, N):
            for k in range(j+1, N):
                if name[0] in dic and names[j][0] in dic and names[k][0] in dic:
                    ans += dic[name[0]] * dic[names[j][0]] * dic[names[k][0]]
    print(ans)


if __name__ == '__main__':
    main()
