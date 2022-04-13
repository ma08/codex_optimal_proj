def main():
    n, p = map(int, input().strip().split())
    d = [int(x) for x in input().strip().split()]
    d.sort()
    min_dist = d[0]
    for i in range(1, n):
        if d[i] - d[i - 1] < p * i:
            min_dist = d[i - 1] + p * i
    print(min_dist)

if __name__ == "__main__":
    main()
