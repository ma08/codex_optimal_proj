
def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i, n):
            if p[i:j+1].count(m) > 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
