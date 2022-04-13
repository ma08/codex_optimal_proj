
n = int(input())   #number of items
price = [int(input()) for i in range(n)]   #list of prices
price.sort()   #sorting prices
print(sum(price[1:]) + price[0]//2)   #adding prices
