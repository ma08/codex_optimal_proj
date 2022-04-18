

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - max(a) if n % 2 == 0 or n == 4 else sum(a) - min(a))

if __name__ == "__main__":
    main()
