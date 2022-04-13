

def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append([int(x) for x in input().split()])
    a = [0] * n
    for i in range(n):
        a[i] = a[i] ^ m[i][i]
    for i in range(n):
        a[i] = a[i] ^ m[i][(i + 1) % n]
    print(*a)

if __name__ == "__main__":
    main()
