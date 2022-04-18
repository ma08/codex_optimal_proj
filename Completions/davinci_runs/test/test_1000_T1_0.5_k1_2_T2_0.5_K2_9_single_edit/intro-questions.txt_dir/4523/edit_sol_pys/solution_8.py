

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print("YES")
        else:
            print("YES" if len(set(a)) == 1 else "NO")

if __name__ == "__main__":
    main()
