

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        cnt = 0
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                cnt += 1
        if cnt == 0:
            break
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
