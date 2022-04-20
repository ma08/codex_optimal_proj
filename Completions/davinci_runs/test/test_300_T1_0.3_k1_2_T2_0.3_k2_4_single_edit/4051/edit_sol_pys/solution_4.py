

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[-1] - a[0] >= 2:
        print("NO")
    else:
        print("YES")

main()
