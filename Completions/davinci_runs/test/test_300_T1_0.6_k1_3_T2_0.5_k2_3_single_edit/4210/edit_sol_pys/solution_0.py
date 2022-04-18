
def is_divisible(n, k):
    return n % k == 0

def solve(n, k, arr):
    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if is_divisible(arr[i] + arr[j], k):
                count += 1
            j += 1
        i += 1
    return count

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))

if __name__ == "__main__":
    main()
