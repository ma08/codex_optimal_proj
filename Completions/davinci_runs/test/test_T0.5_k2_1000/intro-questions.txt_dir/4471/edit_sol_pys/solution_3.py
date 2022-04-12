

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            if a[0] == 1:
                print("NO")
            else:
                print("YES")
            continue
        a.sort()
        if a[0] == 1 and a[1] == 1 and a[2] == 1:
            print("NO")
            continue
        print("YES")

if __name__ == "__main__":
    main()
