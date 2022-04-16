
def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a[::2]) - sum(a[1::2]))

if __name__ == "__main__":
    main()
