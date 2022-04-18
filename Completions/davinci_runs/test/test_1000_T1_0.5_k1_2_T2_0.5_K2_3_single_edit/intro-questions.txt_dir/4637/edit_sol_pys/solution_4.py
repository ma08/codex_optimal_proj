
def max_sum_after_k_swaps(a, b, k, n):
    if k == 0:
        return sum(a)
    else:
        if a[n-1] > b[0]:
            return max_sum_after_k_swaps(a, b[1:], k-1, n)
        else:
            sum_a = sum(a)
            sum_b = sum(b)
            a[-1] = b[0]
            b[0] = 0
            return max(sum_a, sum_b, max_sum_after_k_swaps(a, b, k-1, n))

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(max_sum_after_k_swaps(a, b, k, n))

if __name__ == '__main__':
    main()
