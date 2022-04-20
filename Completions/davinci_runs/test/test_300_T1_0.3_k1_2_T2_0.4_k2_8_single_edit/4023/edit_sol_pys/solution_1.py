

def main():
    n = int(input())
    a = [int(i) for i in input().split()].sort()
    if a[0] == a[n-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
