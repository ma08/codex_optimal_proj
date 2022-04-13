

s = input()
cards = [0]*52
for i in range(0, len(s), 3):
    cards[int(s[i+1:i+3])-1] += 1

print("GRESKA" if any(cards[i] > 1 for i in range(52)) else "{} {} {} {}".format(*(13-cards[i*13:(i+1)*13].count(0) for i in range(4))), end='')
