

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(max(a))
        return
    if n == 3:
        print(sum(a) - min(a))
        return
    if n == 4:
        print(sum(a) - max(a))
        return
    if n % 2 == 0:
        print(sum(a) - max(a))
        return
    print(sum(a) - min(a))

if __name__ == "__main__":
    main()