

def main():
    n, k = map(int, input().split())
    if n < k:
        print("NO")
        return
    if n == 1:
        print("YES")
        print("1")
        return
    if k == 1:
        print("YES")
        print(n)
        return
    if k == 2:
        if n % 2 == 0:
            print("YES")
            print(n//2, n//2)
        else:
            print("NO")
        return
    if n % (k-1) == 0:
        print("YES")
        print(n//(k-1), end=" ")
        for i in range(k-2):
            print(n//(k-1), end=" ")
        print(n//(k-1)+n%(k-1))
        return
    if n % (k-1) == 1:
        print("YES")
        print(n//(k-1), end=" ")
        for i in range(k-3):
            print(n//(k-1), end=" ")
        print(n//(k-1)+1, n//(k-1)+1)
        return
    if n % (k-1) == k-2:
        print("YES")
        print(n//(k-1), end=" ")
        for i in range(k-3):
            print(n//(k-1), end=" ")
        print(n//(k-1)+1, n//(k-1)+2)
        return
    print("NO")
    return

if __name__ == "__main__":
    main()
