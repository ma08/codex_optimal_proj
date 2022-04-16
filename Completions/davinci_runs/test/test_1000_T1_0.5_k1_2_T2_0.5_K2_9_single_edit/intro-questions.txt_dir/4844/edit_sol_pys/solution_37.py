
def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append([int(x) for x in input().split()])
    print(*[sum(m[i]) % 2 for i in range(n)])

if __name__ == "__main__":
    main()
