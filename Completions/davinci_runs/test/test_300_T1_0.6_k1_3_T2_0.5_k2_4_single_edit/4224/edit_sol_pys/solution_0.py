

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        ans = 0
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                cnt += 1
        if cnt == 0:
            break
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
