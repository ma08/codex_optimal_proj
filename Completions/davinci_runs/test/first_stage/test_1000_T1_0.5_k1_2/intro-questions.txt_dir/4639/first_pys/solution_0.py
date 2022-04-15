

#import sys

#sys.stdin = open('in.txt', 'r')

#sys.stdout = open('out.txt', 'w')

def gen(n, k):
    if n == 3:
        if k == 1:
            return 'abb'
        elif k == 2:
            return 'bab'
        else:
            return 'baa'
    else:
        if k <= n-1:
            return 'a' + gen(n-1, k)
        else:
            return 'b' + gen(n-1, k-(n-1))

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n, k = map(int, raw_input().split())
        print gen(n, k)