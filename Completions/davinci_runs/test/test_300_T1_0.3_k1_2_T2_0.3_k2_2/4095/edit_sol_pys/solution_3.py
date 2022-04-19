

def median(arr):
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2
    else:
        return arr[int(len(arr)/2)]

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(arr[i:j+1]) == m:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
