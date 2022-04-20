


def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h_min = min([abs(t - h[i] * 0.006 - a) for i in range(n)])
    print(h.index(h[min([i for i in range(n) if abs(t - h[i] * 0.006 - a) == h_min])]) + 1)


if __name__ == '__main__':
    main()