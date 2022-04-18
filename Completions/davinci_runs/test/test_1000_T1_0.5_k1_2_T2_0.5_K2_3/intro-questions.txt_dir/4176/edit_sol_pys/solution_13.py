import math

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a, b, c = A[i], A[j], A[k]
                if a == b or b == c or c == a:
                    continue
                if a + b > c and a + c > b and b + c > a:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
