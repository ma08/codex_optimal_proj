

# My solution:

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    for i in range(n):
        f = 0
        for j in range(m - 1):
            f += abs(x[j] - x[j + 1])
        print(f, end=' ')
    

if __name__ == "__main__":
    main()
