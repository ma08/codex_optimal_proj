

def main():
    n = int(input())
    print(sum(len(list(filter(lambda x: x[0] * x[1] + x[2] == n, itertools.product(range(1, a + 1), range(1, b + 1), range(1, n + 1))))) for a in range(1, n) for b in range(n - a, n)))

if __name__ == '__main__':
    main()
