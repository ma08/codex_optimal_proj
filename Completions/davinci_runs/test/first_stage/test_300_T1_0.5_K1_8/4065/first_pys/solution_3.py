

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    res = 1
    curr = a[0]
    for i in range(1, n):
        if a[i] > 2 * curr:
            curr = a[i]
            res += 1
    print(res)


if __name__ == "__main__":
    main()