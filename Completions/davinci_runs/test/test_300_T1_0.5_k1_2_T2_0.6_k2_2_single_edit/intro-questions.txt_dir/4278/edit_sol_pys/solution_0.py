
import sys
import heapq


# My code here
def main():
    s = input()
    n = int(input())
    S = [input() for _ in range(n)]
    S.sort()
    for ss in S:
        if ss in s:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
