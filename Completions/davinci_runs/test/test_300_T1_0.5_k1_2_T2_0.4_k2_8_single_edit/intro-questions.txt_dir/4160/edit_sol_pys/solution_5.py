x = int(input())
a = 0
b = 1
for i in range(x):
    a, b = b, a + b
print(a)



# x = int(input())
# year = 0
# balance = 100
# while balance < x:
#     balance += balance // 100
#     year += 1
# print(year)
