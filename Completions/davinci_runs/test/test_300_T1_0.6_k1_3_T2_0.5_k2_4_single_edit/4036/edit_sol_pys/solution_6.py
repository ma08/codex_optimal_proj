

def main():
    n, k = [int(x) for x in input().split()]  # 2 <= k <= n <= 10^5
    if n % (k - 1) == 0:
        print("YES")  # k >= 2
        print("1 " * (k - 1) + str(n // (k - 1)))  # 1 <= x_1 <= x_2 <= ... <= x_k
    elif n % (k - 1) == 1:
        print("NO")
    else:  # 2 <= n % (k - 1) <= k - 2
        print("YES")
        print(str(2 * (n % (k - 1))) + " " + "1 " * (k - 2) + str(n // (k - 1)))


if __name__ == "__main__":
    main()
