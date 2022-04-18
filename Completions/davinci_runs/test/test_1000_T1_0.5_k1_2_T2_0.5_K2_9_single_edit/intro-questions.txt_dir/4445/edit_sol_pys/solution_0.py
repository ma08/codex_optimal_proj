

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    elif n == 2:
        print(max(a))
        return
    elif n == 3:
        print(sum(a) - min(a))
        return
    elif n == 4:
        print(sum(a) - max(a))
        return
    elif n % 2 == 0:
        print(sum(a) - max(a))
        return
    print(sum(a) - min(a))

if __name__ == "__main__":
    main()
