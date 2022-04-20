

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_a = min(a)  # O(n)
    max_a = max(a)  # O(n)
    if min_a == max_a:  # O(1)
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
