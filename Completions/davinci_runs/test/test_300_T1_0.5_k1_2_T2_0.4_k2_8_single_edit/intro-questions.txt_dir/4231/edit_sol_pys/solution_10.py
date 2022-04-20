

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]
    print(ans)

if __name__ == '__main__':
    main()
