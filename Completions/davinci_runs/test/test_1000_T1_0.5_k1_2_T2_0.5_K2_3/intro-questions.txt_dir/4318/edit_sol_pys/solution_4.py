def main(n, h):
    h.sort()
    return h.index(h[0]) + 1


if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split()))
    print(main(n, h))
