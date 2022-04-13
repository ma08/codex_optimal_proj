

def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append([int(x) for x in input().split()])
    a = []
    a.append(0)
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] = a[i] ^ m[i][j]
    print(*a)

if __name__ == "__main__":
    main()
