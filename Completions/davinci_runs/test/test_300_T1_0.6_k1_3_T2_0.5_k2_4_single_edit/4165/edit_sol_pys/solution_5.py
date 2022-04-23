

def main():
    n = int(input())
    lengths = list(map(int, input().split()))

    print("Yes") if (max(lengths) < sum(lengths) - max(lengths)) else print("No")

if __name__ == '__main__':
    main()
