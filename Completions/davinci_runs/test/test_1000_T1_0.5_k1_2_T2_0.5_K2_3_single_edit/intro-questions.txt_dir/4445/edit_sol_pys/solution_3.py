

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n <= 4:
        print(sum(a) - min(a))
    else:
    if n % 2 == 0:
        print(sum(a) - max(a))
    else:
        print(sum(a) - min(a))

if __name__ == "__main__":
    main()
