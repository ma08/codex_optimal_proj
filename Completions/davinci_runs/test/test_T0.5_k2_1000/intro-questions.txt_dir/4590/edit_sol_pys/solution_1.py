
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a)


if __name__ == '__main__':
    main()
