

n = int(input())
cards = input().split(" ")

counts = {}

for card in cards:
    if card in counts.keys():
        counts[card] += 1
    else:
        counts[card] = 1
 
print(max(counts.values()))
