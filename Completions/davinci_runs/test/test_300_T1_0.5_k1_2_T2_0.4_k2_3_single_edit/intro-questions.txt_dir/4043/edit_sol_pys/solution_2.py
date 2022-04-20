

def main():
    n, d, k = [int(x) for x in input().split()]
    if n <= d * k + 1:
        print("YES")
        for i in range(2, d+1):
            print("1 {}".format(i))
        for i in range(d+1, n+1):
            print("{} {}".format(i-d, i))
    else:
        print("NO")

if __name__ == '__main__':
    main()
