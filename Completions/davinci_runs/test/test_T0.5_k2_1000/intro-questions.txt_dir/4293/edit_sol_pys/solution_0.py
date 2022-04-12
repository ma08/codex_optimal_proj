
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    C.sort()
    ans = 0
    for b in B:
        a = bisect_left(A, b)
        c = bisect_right(C, b)
        ans += a * (N-c)
    print(ans)

if __name__ == "__main__":
    main()
