
import sys
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return map(int, input().split())


s = input()

if int(s[2:]) >= 1 and int(s[2:]) <= 12 and int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('YYMM')
    else:
        print('NA')
