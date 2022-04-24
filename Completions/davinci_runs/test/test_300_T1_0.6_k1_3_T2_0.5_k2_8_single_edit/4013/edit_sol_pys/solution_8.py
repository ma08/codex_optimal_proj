

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(min(a[-1] - a[1], a[-2] - a[0]))


if __name__ == '__main__':
    main()

n = int(input())
a = list(map(int, input().split()))

a.sort()

print(min(a[-1] - a[1], a[-2] - a[0]))
