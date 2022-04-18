

def main(n, d):
    c = [0] * (n + 1)
    for i in range(n):
        c[d[i]] += 1
    print(" ".join(map(str, c[1:])))


if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    main(n, d)
