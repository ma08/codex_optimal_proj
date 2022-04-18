
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dorm_sums = [0]
    for i in range(n):
        dorm_sums.append(dorm_sums[i] + a[i])

    for query in b:
        for i in range(1, n+1):
            if dorm_sums[i] >= query:
                print(i, query - dorm_sums[i-1])
                break

if __name__ == "__main__":
    main()
