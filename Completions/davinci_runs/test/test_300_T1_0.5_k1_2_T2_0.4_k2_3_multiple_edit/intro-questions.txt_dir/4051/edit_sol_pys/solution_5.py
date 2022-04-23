

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    for i in range(m+1):
        for j in range(n):
            if a[j] >= m + 1 - i:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print(a)
    print("Yes" if sorted(a) == a else "No")

main()
