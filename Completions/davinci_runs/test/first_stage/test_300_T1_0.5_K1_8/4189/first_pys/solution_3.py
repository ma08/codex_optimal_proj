

n = int(input())
cheeses = {}
for i in range(n):
    cheese = input().split()
    if cheese[0] not in cheeses:
        cheeses[cheese[0]] = cheese[1]
    else:
        cheeses[cheese[0]] = cheeses[cheese[0]] + " " + cheese[1]

print(len(cheeses))