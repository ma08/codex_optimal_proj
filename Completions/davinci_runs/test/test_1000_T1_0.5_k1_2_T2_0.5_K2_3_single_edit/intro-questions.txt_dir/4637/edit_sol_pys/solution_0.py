

def max_sum_after_k_swaps(arr, k):
    arr.sort(reverse=True)
    return sum(arr[:k])

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        print(max_sum_after_k_swaps(arr, k))

if __name__ == '__main__':
    main()
