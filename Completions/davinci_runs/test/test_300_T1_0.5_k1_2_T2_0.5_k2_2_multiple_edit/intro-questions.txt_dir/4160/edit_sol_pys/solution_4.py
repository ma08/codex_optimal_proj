

# x = int(input())  # вводим сумму которую надо накопить
# year = 0
# balance = 100  # начальный баланс
# while balance < x:
#     balance += balance // 100  # процент прибыли
#     year += 1
# print(year)

#
# def fun(x):
#     if x == 0:
#         return 1
#     return x * fun(x - 1)
#
#
# print(fun(5))


# def fun(x):
#     if x == 0:
#         return 1
#     return x * fun(x - 1)
#
#
# print(fun(5))

# def fun(x):
#     if x == 0:
#         return 1
#     return x * fun(x - 1)
#
#
# print(fun(5))


def fun(x):
    if x == 0:
        return 1
    return x * fun(x - 1)


print(fun(5))
