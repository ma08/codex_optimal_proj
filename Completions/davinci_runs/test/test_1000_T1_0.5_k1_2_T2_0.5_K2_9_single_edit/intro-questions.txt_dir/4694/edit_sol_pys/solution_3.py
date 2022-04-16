

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    print(a)

    min_dist = a[0] - a[-1]
    for i in range(n - 1):
        min_dist += a[i] - a[i + 1]
    print(min_dist)

if __name__ == '__main__':
    main()
