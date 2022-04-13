# n, p, m = [int(x) for x in input().split()]
# players = {}

# for i in range(n):
#     players[input()] = 0

# for i in range(m):
#     player, points = input().split()
#     players[player] += int(points)
#     if players[player] >= p:
#         print(player + " wins!")
#         break
# else:
#     print("No winner!")




# for i in range(int(input())):
#     a, b, c = [int(x) for x in input().split()]
#     if a + b == c:
#         print("Possible")
#     elif a - b == c:
#         print("Possible")
#     elif a * b == c:
#         print("Possible")
#     elif a / b == c:
#         print("Possible")
#     elif a % b == c:
#         print("Possible")
#     else:
#         print("Impossible")


# for i in range(int(input())):
#     a, b = [int(x) for x in input().split()]
#     if a == b:
#         print(0)
#     elif a < b:
#         if (b - a) % 2 == 0:
#             print(2)
#         else:
#             print(1)
#     else:
#         if (a - b) % 2 == 0:
#             print(1)
#         else:
#             print(2)


# for i in range(int(input())):
#     s = input()
#     if s == s[::-1]:
#         print("YES")
#     else:
#         print("NO")


print(list(map(lambda x: x ** 2, map(int, input().split()))))
