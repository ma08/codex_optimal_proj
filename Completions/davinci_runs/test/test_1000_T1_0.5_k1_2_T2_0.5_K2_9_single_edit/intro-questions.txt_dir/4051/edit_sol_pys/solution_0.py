

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    for i in range(m+1):
        for j in range(n):
            if a[j] >= m - i + 1:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print(a)
    print("YES" if sorted(a) == a else "NO")

main()
