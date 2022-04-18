
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print("YES")
        else:
            if len(set(a)) == 1 and a[0] == 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
