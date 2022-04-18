

def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    arr.sort()
    count = 0
    for i in range(0, n, 2):
        count += arr[i+1] - arr[i]
    print(count)


if __name__ == "__main__":
    main()
