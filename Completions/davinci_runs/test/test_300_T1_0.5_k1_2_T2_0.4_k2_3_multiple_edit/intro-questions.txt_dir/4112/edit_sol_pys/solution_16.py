

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if k < x:
        print(-1)
        return
    ans = 0
    for i in range(k):
        if i < n:
            ans += A[i]
        else:
            ans += x
    print(ans)
    return

if __name__ == '__main__':
    main()
