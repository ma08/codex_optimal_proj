

def main():
    n = int(input())
    a = [int(x) for x in input().split()].sort()
    print("YES" if a[-1] - a[0] <= 1 else "NO")

main()
