
def max_sum_after_k_swaps(a, b, k):
    arr = sorted(a + b)
    return sum(arr[-k:]) + sum(arr[:n - k])

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
