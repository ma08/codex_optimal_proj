
def check(a):
    for i in range(len(a)):
        if a[i] == a[0]:
            a[i] = 1
        elif a[i] != a[0]:
            a[i] = 2
    return a
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print("YES")
        print(1)
    else:
        b = [0] * n
        for i in range(n):
            if a[i] == a[0]:
                b[i] = 1
            else:
                b[i] = 2
        if a[0] in a[1:]:
            print("NO")
        else:
            print("YES")
            print(*b)
main()
