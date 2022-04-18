

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(sum(a) - max(a))
    print(sum(b) - max(b))

if __name__ == "__main__":
    main()
