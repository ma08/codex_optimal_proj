

# This is a comment

cards = input().split(" ")

counts = {}

for card in cards:
    if card[0] in counts:
        counts[card[0]] = counts[card[0]] + 1
    else:
        counts[card[0]] = 1

print(max(counts.values()))
