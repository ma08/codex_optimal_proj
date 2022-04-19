

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_a, max_a = min(a), max(a)
    if min_a != max_a:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
