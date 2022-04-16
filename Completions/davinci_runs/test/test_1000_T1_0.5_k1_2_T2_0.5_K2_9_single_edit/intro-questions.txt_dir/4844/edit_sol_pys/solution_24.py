

def main():
    n = int(input())
    m = [int(x) for x in input().split()]
    m = [m[i:i+n] for i in range(0, len(m), n)]
    a = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] = a[i] ^ m[i][j]
    print(*a)

if __name__ == "__main__":
    main()
