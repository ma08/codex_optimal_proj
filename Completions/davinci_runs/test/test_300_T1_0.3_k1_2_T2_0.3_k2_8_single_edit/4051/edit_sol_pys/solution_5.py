

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[-1] - a[0] > 1 or a[0] == a[-1]:
        print("NO")
    else:
        print("YES")

main()
