
def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
    for i in range(1, n + 1):
        if i in d:
            print(d[i])
        else:
            print(0)

if __name__ == "__main__":
    main()
