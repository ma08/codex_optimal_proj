

n = int(input())
chips = list(map(int, input().split()))

min_chip = min(chips)
min_chip_count = chips.count(min_chip)

# print(min_chip)
# print(min_chip_count)

min_cost = 0

for i in range(n):
    if chips[i] > min_chip:
        min_cost += chips[i] - min_chip

if min_chip_count == 1:
    min_cost += 1

print(min_cost)