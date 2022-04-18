def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if n == 1:
        print(a[0])
    else:
        print(a[0] + a[1])



if __name__ == "__main__":
    main()
