

def main():
    n = int(input())
    a = [int(i) for i in input().split()].sort()
    print("YES" if a[0] == a[-1] else "NO")

if __name__ == "__main__":
    main()
