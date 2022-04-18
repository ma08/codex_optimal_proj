

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(sum(a) - min(a), sum(a) - max(a)))

if __name__ == "__main__":
    main()
