

s = input()
cards = [0]*52
for i in range(0, len(s), 3):
    cards[int(s[i+1:i+3])-1] += 1

print("GRESKA" if any(cards[i] > 1 for i in range(52)) else "{} {} {} {}".format(13-cards[:13].count(1),
                                                                                 13-cards[13:26].count(1),
                                                                                 13-cards[26:39].count(1),
                                                                                 13-cards[39:52].count(1)))
