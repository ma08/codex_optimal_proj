

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = [int(x) for x in input().split()]
        a = list(range(1,n+1))
        for j in range(n):
            temp = a[p[j]-1]
            a[p[j]-1] = a[j]
            a[j] = temp
        if a == list(range(1,n+1)):
            print(*[1] * n)
        else:
            count = 0
            while a != list(range(1,n+1)):
                count += 1
                temp = a[p[a[0]-1]-1]
                a[p[a[0]-1]-1] = a[0]
                a[0] = temp
            print(*[count] * n)

main()
