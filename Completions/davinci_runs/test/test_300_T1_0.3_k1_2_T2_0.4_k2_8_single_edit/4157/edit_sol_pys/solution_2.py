

def main():
    n = int(input())
    a = list(map(int, input().split()))  # map(function, iterable)
    a.sort()
    a.reverse()
    print(*a)

if __name__ == "__main__":
    main()
