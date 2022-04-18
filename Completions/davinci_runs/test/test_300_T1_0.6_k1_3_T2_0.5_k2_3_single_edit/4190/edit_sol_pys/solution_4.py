

#-----Solution-----

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(a[i]+b[i])

    l = []
    for i in range(n):
        l.append(c[i]%n+1)

    print(*l)

main()
