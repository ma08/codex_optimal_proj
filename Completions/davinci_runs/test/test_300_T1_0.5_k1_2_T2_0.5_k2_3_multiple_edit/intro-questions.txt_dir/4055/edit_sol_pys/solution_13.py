

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if (a[i-1] == 1 and a[i+1] == 1 and a[i] == 0):  # if the left and right of the current index is 1 and the current index is 0 then count++
            count += 1
    print(count)


if __name__ == "__main__":
    main()
