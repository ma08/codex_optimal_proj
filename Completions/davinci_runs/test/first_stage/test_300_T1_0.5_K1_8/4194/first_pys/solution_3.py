

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum_A = sum(A)
    if sum_A > N:
        print(-1)
        exit()
    ans = N - sum_A
    for a in A:
        if ans > 0:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()