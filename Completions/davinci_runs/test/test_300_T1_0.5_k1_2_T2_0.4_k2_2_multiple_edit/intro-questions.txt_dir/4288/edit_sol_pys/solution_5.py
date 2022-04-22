

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == A[i+1]:
            ans += 1
            i += 1
    print(ans)

if __name__ == '__main__':
    main()
