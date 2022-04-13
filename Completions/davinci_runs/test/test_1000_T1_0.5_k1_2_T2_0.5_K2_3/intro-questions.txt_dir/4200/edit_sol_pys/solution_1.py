

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * k):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
