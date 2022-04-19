

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append((a[i]+b[i])%n)
    c.sort()
    print(*c)

if __name__ == "__main__":
    main()