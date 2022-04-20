
def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    a.sort()
    count = 0
    for i in range(0, n, 2):
        count += a[i+1] - a[i]
    print(count)


if __name__ == "__main__":
    main()
