

def concat(a, b):
    return int(str(a) + str(b))

def kaprekar(n):
    n = str(n)
    n1 = int(''.join(sorted(n)))
    n2 = int(''.join(sorted(n)[::-1]))
    return n2 - n1

def is_divisible(a, b, k):
    return concat(a, b) % k == 0

def solve(n, k, arr):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_divisible(arr[i], arr[j], k) and kaprekar(arr[i]) == kaprekar(arr[j]):
                count += 1 
    return count

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))

if __name__ == "__main__":
    main()
