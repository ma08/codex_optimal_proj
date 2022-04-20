

def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        arr = [1]*(n-1)
        if m > n-1:
            arr.append(m - (n-1))
        else:
            arr[-1] = m
        print(arr)
        print(sum([abs(arr[i+1] - arr[i]) for i in range(len(arr)-1)]))


if __name__ == "__main__":
    main()
