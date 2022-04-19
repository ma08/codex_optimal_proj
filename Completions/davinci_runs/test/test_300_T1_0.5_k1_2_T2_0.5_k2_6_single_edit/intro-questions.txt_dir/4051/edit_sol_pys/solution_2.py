

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a) + 1
    for i in range(m, 0, -1):
        for j in range(n):
            if a[j] >= m - i:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

main()
