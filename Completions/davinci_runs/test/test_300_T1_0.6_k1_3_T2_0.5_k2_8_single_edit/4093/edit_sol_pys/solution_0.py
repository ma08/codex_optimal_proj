

def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        arr = [1]*(n-1) + [m - (n-1)]
        print(sum([abs(arr[i+1] - arr[i]) for i in range(n-1)]))


if __name__ == "__main__":
    main()
