#
# n, k = map(int, input().split())
# s = input()
#
# # if k > n or k == 0:
# #     print(-1)
# # else:
# #     print(n - k)
#
# if k > n or k == 0:
#     print(-1)
# else:
#     print(n - k)


# n, k = map(int, input().split())
# s = input()
#
# # if k > n or k == 0:
# #     print(-1)
# # else:
# #     print(n - k)
#
# if k > n or k == 0:
#     print(-1)
# else:
#     print(n - k)

n, k = map(int, input().split())  # 標準入力
s = input()  # 標準入力

if k > n:  # kがnより大きい時
    print(-1)  # -1を出力
else:
    print(n - k)  # kがnより小さい時、n-kを出力
