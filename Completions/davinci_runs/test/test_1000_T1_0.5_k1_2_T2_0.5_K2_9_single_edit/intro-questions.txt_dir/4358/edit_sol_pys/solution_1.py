
n = int(input())
price = [int(input()) for i in range(n)]
price.sort()
print(sum(price[1:]) + price[0] // 2)
