def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        print(arr[n // 2])

if __name__ == '__main__':
    main()
