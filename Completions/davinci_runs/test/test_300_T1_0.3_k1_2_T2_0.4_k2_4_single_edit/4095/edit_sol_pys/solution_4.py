

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(sum([p[i:j+1].count(m) for i in range(n) for j in range(i, n)]))

if __name__ == "__main__":
    main()
