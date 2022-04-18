
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())  # a, b = input().split()
    ans = 0
    if a < b:
        if (b - a) % 2 == 0:
            ans = 1
        else:
            ans = 2
    elif a > b:
        if (a - b) % 2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        ans = 0

# a, b = map(int, input().split())
# print(a, b)
# print(type(a), type(b))
#
# # a = int(input())
# # b = int(input())
# # print(a, b)
# # print(type(a), type(b))
    print(ans)
