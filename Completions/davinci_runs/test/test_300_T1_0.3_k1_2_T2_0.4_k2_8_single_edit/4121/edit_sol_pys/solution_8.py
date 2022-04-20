

def main():
    n = int(input())
    s = list(map(int, input().split()))
    min_s = min(s)
    max_s = max(s)
    if min_s == max_s:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
