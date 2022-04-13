

def main():
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    print(arr)
    if arr[0] == arr[-1]:
        print(arr[0])
    else:
        print(-1)

if __name__ == "__main__":
    main()
