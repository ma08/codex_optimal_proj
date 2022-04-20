

def main():
    n = int(input())
    b = set(a)
    a = list(map(int, input().split()))
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a and len(b) == 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
