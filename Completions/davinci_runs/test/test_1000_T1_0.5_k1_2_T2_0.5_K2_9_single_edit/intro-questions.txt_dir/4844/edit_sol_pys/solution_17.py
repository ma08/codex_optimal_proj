

def main():
    n = int(input())
    m = [int(x) for x in input().split()]
    a = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] = a[i] ^ m[j]
    print(*a)

if __name__ == "__main__":
    main()
