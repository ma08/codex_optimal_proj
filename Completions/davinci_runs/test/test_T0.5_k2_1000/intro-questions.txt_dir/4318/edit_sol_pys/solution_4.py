
def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)


if __name__ == '__main__':
    main()
