

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    s.reverse()
    print(*s)

if __name__ == "__main__":
    main()
