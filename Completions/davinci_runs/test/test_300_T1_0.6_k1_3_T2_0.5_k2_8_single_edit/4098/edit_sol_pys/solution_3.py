

# def solve(n, k, a):
#     a.sort()
#     a.append(a[-1] + 5)
#     #print(a)
#     cnt = 0
#     for i in range(n):
#         if i == 0 or a[i] - a[i-1] > 5:
#             cnt += 1
#             if cnt == k + 1:
#                 return i
#     return n

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# print(solve(n, k, a))


def solve(a):
    if a == 1:
        print(1)
        return
    if a == 2:
        print(2)
        return
    if a == 3:
        print(3)
        return
    if a % 2 == 0:
        print(2)
        return
    print(3)


a = int(input())
solve(a)
