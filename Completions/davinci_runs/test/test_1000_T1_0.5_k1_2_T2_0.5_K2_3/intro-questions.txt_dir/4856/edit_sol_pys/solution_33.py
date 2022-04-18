
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for i in range(n):
        print(a[i] + b[i])


if __name__ == "__main__":
    main()
