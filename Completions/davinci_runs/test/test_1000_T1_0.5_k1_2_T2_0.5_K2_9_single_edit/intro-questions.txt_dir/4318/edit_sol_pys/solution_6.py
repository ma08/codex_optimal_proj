def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(h.index(h[0]) + 1)



def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(h.index(h[0]) + 1)


if __name__ == '__main__':
    main()
