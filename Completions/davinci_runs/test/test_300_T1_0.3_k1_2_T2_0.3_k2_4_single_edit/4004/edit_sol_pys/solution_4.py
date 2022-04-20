

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    a.sort()  # O(nlogn)
    if a[0] == a[-1]:
        print(0)
    elif a[0] + 1 == a[-1]:
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
