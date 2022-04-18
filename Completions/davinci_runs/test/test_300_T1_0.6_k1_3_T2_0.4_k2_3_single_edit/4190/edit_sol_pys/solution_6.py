
#-----Solution-----

def main():
    n = int(input())  # number of elements
    a = list(map(int, input().split()))  # array a
    b = list(map(int, input().split()))  # array b
    c = []  # sum of a and b
    for i in range(n):  # sum of a and b
        c.append(a[i]+b[i])  # sum of a and b

    c.sort()  # sort c
    l = []  # list of remainder
    for i in range(n):  # remainder
        l.append(c[i] % n)  # remainder

    print(*l)

main()
