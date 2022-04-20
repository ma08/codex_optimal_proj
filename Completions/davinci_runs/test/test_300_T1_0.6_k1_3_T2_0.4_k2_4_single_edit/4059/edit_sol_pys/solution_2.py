

def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        b = n - a
        ans += len(list(filter(lambda x: x[0] * x[1] + x[2] == n, itertools.product(range(1, a + 1), range(1, b + 1), range(1, n + 1))))
    print(ans)

if __name__ == '__main__':
    main()
