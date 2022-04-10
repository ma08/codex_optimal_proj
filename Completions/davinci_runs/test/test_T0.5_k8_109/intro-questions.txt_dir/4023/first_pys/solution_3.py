

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if len(set(a)) == 1:
        print("YES")
        return
    for i in range(1, n):
        if a[i] != a[i - 1]:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()