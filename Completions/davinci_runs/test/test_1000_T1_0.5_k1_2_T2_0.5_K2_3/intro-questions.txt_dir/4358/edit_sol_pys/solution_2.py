# author: zac
# create-time: 2019-10-24 17:46
# usage: - 

n = int(input())
price = [int(input()) for i in range(n)]
price.sort()
print(sum(price[1:]) + price[0] // 2)
