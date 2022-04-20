

import sys

def main():
    N, M = map(int, input().split())
    dic = dict.fromkeys(range(1, M+1), 0)
    for _ in range(N):
        for i in map(int, sys.stdin.readline().split()[1:]):
            dic[i] += 1
    print(sum([1 for e in dic.values() if e == N]))

if __name__ == '__main__':
    main()
