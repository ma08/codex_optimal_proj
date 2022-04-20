

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[-1] - a[0] > 1 or a.count(a[-1]) > n // 2:
        print("NO")
    else:
        print("YES")

main()
