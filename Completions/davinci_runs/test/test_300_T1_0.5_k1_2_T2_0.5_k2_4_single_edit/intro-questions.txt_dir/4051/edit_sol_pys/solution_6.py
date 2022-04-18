

def sorting(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorting(a)
    m = max(a)
    for i in range(m):
        for j in range(n):
            if a[j] >= m - i:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print("YES" if sorted(a) == a else "NO")

main()
