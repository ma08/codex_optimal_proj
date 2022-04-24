

def main():
    n = int(input())
    a = input().split()
    a.sort(key=int)
    # a = [int(x) for x in a]
    # a.sort()
    count = 0
    for i in range(0, n, 2):
        count += int(a[i+1]) - int(a[i])
    print(count)


if __name__ == "__main__":
    main()
