
import math

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = []
    for i in range(N):
        H.append(float(input()))
    ans = 0
    min_val = math.inf
    for i in range(N):
        val = abs(T - 0.006 * H[i] - A)
        if val < min_val:
            ans = i
            min_val = val
    print(ans+1)

if __name__ == '__main__':
    main()
