

def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    m = 0
    for i in range(n - 1):
        if s[i + 1] - s[i] <= 5:
            m += 1
    print(m + 1)


if __name__ == '__main__':
    main()
