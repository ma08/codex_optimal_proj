

def max_sum_after_k_swaps(a, b, k):
    n = len(a)
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if i < k:
            if a[i] < b[n - i - 1]:
                a[i], b[n - i - 1] = b[n - i - 1], a[i]
        ans += a[i]
    return ans

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(max_sum_after_k_swaps(a, b, k))

if __name__ == '__main__':
    main()
