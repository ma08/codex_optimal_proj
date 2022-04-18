
import math

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A = sorted(A)
    C = sorted(C)
    ans = 0
    for b in B:
        lower = bisect_left(A,b)
        upper = bisect_right(C,b)
        ans += lower*(N-upper)
    print(ans)

main()
