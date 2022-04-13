

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - min(a) if n % 2 == 0 else sum(a) - max(a))

if __name__ == "__main__":
    main()
