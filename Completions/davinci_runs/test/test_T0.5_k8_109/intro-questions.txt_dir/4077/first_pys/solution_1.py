

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            med = median(arr[i:j+1])
            if med == m:
                cnt += 1
    print(cnt)

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return arr[n//2 - 1]
    return arr[n//2]

if __name__ == "__main__":
    main()