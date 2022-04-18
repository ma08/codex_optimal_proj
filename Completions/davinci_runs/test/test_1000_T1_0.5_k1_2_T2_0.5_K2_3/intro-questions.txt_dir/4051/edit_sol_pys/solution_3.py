

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    # m = max(a)
    # for i in range(m):
    #     for j in range(n):
    #         if a[j] >= m - i:
    #             print("#", end="")
    #         else:
    #             print(" ", end="")
    #     print("")
    # print(a)

    # print("YES" if sorted(a) == a else "NO")
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(a[n // 2])


main()
