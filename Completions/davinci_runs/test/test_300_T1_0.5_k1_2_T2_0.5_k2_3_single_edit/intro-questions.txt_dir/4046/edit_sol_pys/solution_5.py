#
#
# def solve(n, q):
#     p = [1]
#     for i in range(n - 1):
#         if p[-1] + q[i] > 0 and p[-1] + q[i] <= n:
#             p.append(p[-1] + q[i])
#         else:
#             return -1
#     return p
#
#
# def main():
#     n = int(input())
#     q = list(map(int, input().split()))
#     print(*solve(n, q))
#
#
# if __name__ == "__main__":
#     main()



def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = ans + b[a[i] - 1]
        if i > 0 and a[i] - a[i - 1] == 1:
            ans = ans + c[a[i] - 2]
    print(ans)




if __name__ == "__main__":
    main()
