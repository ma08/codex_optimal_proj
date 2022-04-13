

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
        if a[0] == 1 and a[1] == 1:
            print("NO")
            continue
        if a[-1] == 1:
            print("YES")
            continue
        if a[0] == 1:
            if a[1] == 2:
                print("NO")
                continue
            else:
                print("YES")
                continue
        if a[-1] == 2:
            print("NO")
            continue
        if a[0] == 2:
            print("YES")
            continue
        if a[0] == 3:
            if a[1] == 3:
                print("NO")
                continue
            else:
                print("YES")
                continue
        print("YES")

if __name__ == "__main__":
    main()