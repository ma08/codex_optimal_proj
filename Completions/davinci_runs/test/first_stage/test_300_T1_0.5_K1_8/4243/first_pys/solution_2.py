

x = int(input())

happiness = x // 500 * 1000
happiness += x % 500 // 5 * 5

print(happiness)