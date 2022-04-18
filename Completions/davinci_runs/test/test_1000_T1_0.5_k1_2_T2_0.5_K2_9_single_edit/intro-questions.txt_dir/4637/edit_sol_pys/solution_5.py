

def max_sum_after_k_swaps(n, k, a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(n):
        res += min(a[i], b[n - i - 1])
    return res - min(k, n) * min(a[0], b[n - 1])

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(max_sum_after_k_swaps(n, k, a, b))

if __name__ == '__main__':
    main()
