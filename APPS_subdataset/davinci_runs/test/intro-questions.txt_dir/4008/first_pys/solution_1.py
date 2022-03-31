

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_set = set(a)
    if len(a_set) > k:
        print("NO")
        return
    color = [0 for _ in range(n)]
    for i in range(n):
        color[i] = (a[i] - 1) % k + 1
    print("YES")
    print(*color)

if __name__ == "__main__":
    main()