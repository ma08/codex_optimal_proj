

x = int(input())

# 100 * 1.01**n >= x
# n >= log(x / 100) / log(1.01)
print(math.ceil(math.log(x / 100) / math.log(1.01)))