import sys
readline = sys.stdin.readline
def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[i]*A[j]
    print(ans)
if __name__ == '__main__':
    main()

import sys

readline = sys.stdin.readline

def main():
    P, Q, R = map(int, readline().split())

    print(min(P+Q, Q+R, R+P))

if __name__ == '__main__':
    main()
