

def concat(a, b):
    return int(str(a) + str(b))

def solve(n, k, a):
    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if concat(a[i], a[j]) % k == 0:
                count += 1
            j += 1
        i += 1
    return count

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

if __name__ == "__main__":
    main()
