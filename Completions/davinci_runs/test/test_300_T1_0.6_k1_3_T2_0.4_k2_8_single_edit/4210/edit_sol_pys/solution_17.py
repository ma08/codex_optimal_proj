

def concat(a, b):
    length = len(str(a))
    return a*10**length + b

def is_divisible(a, b, k):
    return concat(a, b) % k == 0

def solve(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if is_divisible(arr[i], arr[j], k): count += 1
    return count

def main():
    k = int(input())
    arr = list(map(int, input().split()))[1:]
    print(solve(arr, k))

if __name__ == "__main__":
    main()
