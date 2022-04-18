

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    count = 0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if 500 * i + 100 * j + 50 * k == X:
                    count += 1
    print(count)

def main2():
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            c += 1
    print(c)

def main3():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(A[N//2] - A[N//2-1])
    else:
        print(0)

def main4():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(100 ** D * N)

def main5():
    N = int(input())
    S = input()
    K = int(input())
    ans = ''
    for s in S:
        if s == S[K-1]:
            ans += s
        else:
            ans += '*'
    print(ans)

if __name__ == '__main__':
    main()
