
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(enumerate(a, 1))
    a = sorted(a, key=lambda x: x[1], reverse=True)
    a = [i + 1 for i in a]
    print(*a)


if __name__ == '__main__':
    main()
