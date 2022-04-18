
def main():
    n = int(input())
    m = max(a)
    a = list(map(int, input().split()))
    for i in range(m):
        for j in range(n):
            if a[j] >= m - i:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

main()
