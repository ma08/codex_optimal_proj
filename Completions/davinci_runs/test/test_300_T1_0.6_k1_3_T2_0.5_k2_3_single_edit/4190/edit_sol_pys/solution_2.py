

#-----Solution-----

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i]+b[i] for i in range(n)]

    c.sort()
    l = [c[i]%n for i in range(n)]

    print(*l)

main()
