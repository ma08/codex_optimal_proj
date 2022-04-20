

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))[:n]
    count = 0
    for i in range(n):
        for j in range(i, n):
            if p[i:j+1].count(m) > 0 and len(p[i:j+1]) != 1:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
