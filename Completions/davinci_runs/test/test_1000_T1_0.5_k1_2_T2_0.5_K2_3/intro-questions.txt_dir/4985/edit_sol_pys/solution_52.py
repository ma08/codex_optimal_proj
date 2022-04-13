
N = int(input())

cards = [input() for i in range(4*N)]

suits = {'C': 0, 'D': 0, 'H': 0, 'S': 0}

for card in cards: 
    suits[card[1]] += 1

print(suits)
