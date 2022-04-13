
def main():
    n, m = map(int, input().split())
    count = 0
    for x in range(n+1):
        for y in range(m+1):
            if x * y == m:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
