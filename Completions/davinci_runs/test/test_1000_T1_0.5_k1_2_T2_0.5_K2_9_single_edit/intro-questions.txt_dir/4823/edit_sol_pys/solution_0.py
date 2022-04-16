
cards = input().split()

counts = {}

for card in cards:
    counts[card[0]] = counts.get(card[0], 0) + 1

print(max(counts.values()))
