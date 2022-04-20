

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        print("YES")
        return
    a.sort()
    if a[-1] - a[0] > 1:
        print("NO")
    else:
        print("YES")

main()
