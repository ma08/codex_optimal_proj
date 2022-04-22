

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x < k:
        print(-1)
        return
    result = 0
    for i in range(n):
        result = max(result, A[i] + A[i-1])
    print(result)
    return

if __name__ == '__main__':
    main()
