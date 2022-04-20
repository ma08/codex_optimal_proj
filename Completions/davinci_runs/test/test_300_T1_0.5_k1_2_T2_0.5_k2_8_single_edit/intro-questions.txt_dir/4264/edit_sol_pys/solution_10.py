

N = int(input())
# odd_count = 0
# for i in range(1, N + 1):
#     if len(str(i)) % 2 == 1:
#         odd_count += 1

# print(odd_count)



odd_count = 0
for i in range(1, N + 1):  # i は 1 から N までの整数
    if len(str(i)) % 2 == 1:  # i の桁数が奇数なら
        odd_count += 1

print(odd_count)
