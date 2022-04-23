

def main():
    n, d, k = [int(x) for x in input().split()]
    if n <= d * k + 1:
        print("YES")
        for i in range(1, d):
            print("{} {}".format(i, i+1))
        print("\n".join(["{} {}".format(d, x) for x in range(d+1, n+1)]), end='')
    else:
        print("NO")

if __name__ == '__main__':
    main()
