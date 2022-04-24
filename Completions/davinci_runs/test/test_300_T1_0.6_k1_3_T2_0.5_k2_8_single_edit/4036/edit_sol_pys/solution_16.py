

def main():
    n, k = [int(x) for x in input().split()]
    if n < k:
        print("NO")
        return
    if k == 1:
        if n == 1:
            print("YES\n1")
        else:
            print("NO")
        return
    # k >= 2
    if n % (k - 1) != 1:
        print("YES") 
        print(str(2 * (n % (k - 1))) + " " + "1 " * (k - 2) + str(n // (k - 1)))
        return
    print("NO")

if __name__ == "__main__":
    main()
