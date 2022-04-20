

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i:i+m].count(m) > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
