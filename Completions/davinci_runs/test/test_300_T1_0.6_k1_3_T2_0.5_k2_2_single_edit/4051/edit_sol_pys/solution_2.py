

def main():
    n, k = input().split()
    n = int(n)
    k = int(k)

    arr = list(map(int, input().split()))[:n]

    if k == 1:
        print(max(arr))
    elif k == 2:
        print(max(arr[0], arr[n-1]))
    else:
        print(max(arr))



main()
