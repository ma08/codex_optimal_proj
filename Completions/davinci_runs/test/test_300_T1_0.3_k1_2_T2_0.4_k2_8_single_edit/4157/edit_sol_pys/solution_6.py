

def main():
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    a.reverse()
    print(*a)

if __name__ == "__main__":
    main()
