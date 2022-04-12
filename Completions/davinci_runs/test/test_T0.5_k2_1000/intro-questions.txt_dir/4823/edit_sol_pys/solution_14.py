
cards = input().split() # ['3D', '4S', '5H', '6C', '7D']

counts = {} # {'3': 1, '4': 1, '5': 1, '6': 1, '7': 1}

for card in cards:
    if card[0] in counts:
        counts[card[0]] += 1
    else:
        counts[card[0]] = 1

print(max(counts.values())) # 1
