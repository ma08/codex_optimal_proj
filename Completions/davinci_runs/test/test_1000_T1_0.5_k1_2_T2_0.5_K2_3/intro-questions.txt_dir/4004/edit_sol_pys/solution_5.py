

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = min(a) - 1
    for i in range(n):
        a[i] = a[i] - d - 1
    if sum(a) % n == 0:
        print(d + 1)
    else:
        print(-1)

if __name__ == "__main__":
    main()
