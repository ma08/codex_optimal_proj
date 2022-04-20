

n = int(input())

cheeses = {}

for i in range(n):
    name, type = input().split()
    cheeses[name] = type

soft = 0
hard = 0

for value in cheeses.values():
    if value == "soft":
        soft += 1
    else:
        hard += 1

print(min(soft, hard))