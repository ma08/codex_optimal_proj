

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(max(a))
        return
    print(sum(a) - min(a) - max(a) + 1)

if __name__ == "__main__":
    main()
