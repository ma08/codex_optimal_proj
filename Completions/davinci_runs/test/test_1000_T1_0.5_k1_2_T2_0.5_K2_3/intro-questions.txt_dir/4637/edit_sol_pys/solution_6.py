

def max_sum_after_k_swaps(a, b, k):
    arr = a + b
    arr.sort(reverse=True)
    ans = 0
    j = 0
    while j < k:
        ans += arr[j]
        j += 1
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
