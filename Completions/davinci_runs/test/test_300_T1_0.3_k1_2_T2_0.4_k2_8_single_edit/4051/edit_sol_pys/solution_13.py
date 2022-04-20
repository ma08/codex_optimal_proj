

def main():
    n = int(input())
    a = [int(x) for x in raw_input().split()]
    a.sort()
    if a[-1] - a[0] > 1:
        print("NO")
    else:
        print("YES")

main()
