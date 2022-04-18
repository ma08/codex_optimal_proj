

cards = input().split()  # split by space

counts = {}

for card in cards:
    if card[0] in counts:
        counts[card[0]] = counts[card[0]] + 1
    else:
        counts[card[0]] = 0

print(max(counts.values()))
