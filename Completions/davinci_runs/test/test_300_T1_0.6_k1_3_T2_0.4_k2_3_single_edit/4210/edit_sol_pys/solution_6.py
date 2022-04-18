

def concat(a, b):
    return a*10**len(str(b)) + b

def kaprekar(n):
    n = str(n) 
    n1 = int(''.join(sorted(n)))
    n2 = int(''.join(sorted(n)[::-1]))
    return n2 - n1

def is_divisible(a, b, k):
    return concat(a, b) % k == 0 

def solve(n, k, arr):
    return sum(is_divisible(arr[i], arr[j], k) for i in range(n) for j in range(i + 1, n))

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))

if __name__ == "__main__":
    main()
