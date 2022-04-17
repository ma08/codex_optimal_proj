

def solve(n, a):
    a.sort()
    print(a) 
    for i in range(n-1):
        if a[i+1] - a[i] > 5:
            print(i)
            return i
    return n


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
