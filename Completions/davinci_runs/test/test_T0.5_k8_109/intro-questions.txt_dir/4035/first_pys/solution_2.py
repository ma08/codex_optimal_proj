

# Since the consumption tax rate is 8% and 10%, we can assume the consumption tax rate is 8% + 2% = 10%.
# If the price of a product before tax is a, the amount of consumption tax levied on it is:
#   a * 0.1 = a / 10
# Therefore, the price of a product before tax is:
#   a = 10 * B / 10
# If the price of a product before tax is a, the amount of consumption tax levied on it is:
#   a * 0.08 = a / 12.5
# Therefore, the price of a product before tax is:
#   a = 12.5 * A / 12.5
# If a product satisfies the condition, the following must be true:
#   10 * B / 10 = 12.5 * A / 12.5
#   B * 10 = A * 12.5
#   B * 10 / A = 12.5
#   B * 10 % A = 0

a, b = map(int, input().split())

if (b * 10) % a == 0:
    print((b * 10) // a * 12.5)
else:
    print(-1)