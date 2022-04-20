

def main():
    n = int(input())
    a = [int(i) for i in input().split()]  # a = [1, 2, 3, 4, 5]
    a.sort()
    if a[0] == a[-1]:  # if a[0] == a[4]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
