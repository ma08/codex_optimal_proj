
# n = int(input())
# seats = [0] * 100000  # создаем массив мест из 100000 элементов
# for i in range(n):
#     l, r = map(int, input().split())
#     for j in range(l, r + 1):
#         seats[j - 1] = 1
# print(sum(seats))

# n = int(input())
# a = [int(input()) for i in range(n)]
# print(a)
#
# a = []
# for i in range(n):
#     a.append(int(input()))
# print(a)
#
# a = list(map(int, input().split()))
# print(a)

# n = int(input())
# a = [0] * n
# for i in range(n):
#     a[i] = int(input())
# print(a)

# a = list(map(int, input().split()))
# print(a[0] + a[1])

# a = list(map(int, input().split()))
# print(a)

# a = list(map(int, input().split()))
# print(a[1] + a[2], a[0] + a[2], a[0] + a[1])

# a = list(map(int, input().split()))
# print(a[0] * a[1] + a[2])

# a = list(map(int, input().split()))
# print(a[0] * a[1] + a[2] * a[3])

# a = list(map(int, input().split()))
# print(a[0] * a[1] - a[2])

# a = list(map(int, input().split()))
# print(a[0] * a[1] - a[2] * a[3])

# a = list(map(int, input().split()))
# print(a[0] * a[1] * a[2])

# a = list(map(int, input().split()))
# print(a[0] * a[1] * a[2], a[0] + a[1] + a[2])

# a = list(map(int, input().split()))
# print(a[0] + a[1] + a[2], a[0] * a[1] * a[2])

# a = list(map(int, input().split()))
# print((a[0] + a[1]) / 2, (a[1] + a[2]) / 2, (a[2] + a[0]) / 2)

# a = list(map(int, input().split()))
# print((a[0] + a[1] + a[2]) / 3)

# a = list(map(int, input().split()))
# print((a[0] + a[1] + a[2]) / 3, (a[0] * a[1] * a[2]) ** (1 / 3))

# a = list(map(int, input().split()))
# print((a[0] + a[1] + a[2]) / 3, (a[0] * a[1] * a[2]) ** (1 / 3))

# a = list(map(int, input().split()))
# print(max(a[0], a[1], a[2]))

# a = list(map(int, input().split()))
# print(max(a[0] + a[1], a[1] + a[2], a[2] + a[0]))

a = list(map(int, input().split()))
print(max(a[0] * a[1], a[1] * a[2], a[2] * a[0]))
