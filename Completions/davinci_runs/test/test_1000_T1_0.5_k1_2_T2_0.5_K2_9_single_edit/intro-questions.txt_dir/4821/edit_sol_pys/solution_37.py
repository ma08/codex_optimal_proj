

def main():
    cards = input()
    cards = cards.split(" ")
    p = [0] * 13
    k = [0] * 13
    h = [0] * 13
    t = [0] * 13
    for card in cards:
        if card[0] == "P":
            p[int(card[1:]) - 1] = 1
        elif card[0] == "K":
            k[int(card[1:]) - 1] = 1
        elif card[0] == "H":
            h[int(card[1:]) - 1] = 1
        elif card[0] == "T":
            t[int(card[1:]) - 1] = 1
    if max(p) > 1 or max(k) > 1 or max(h) > 1 or max(t) > 1:
        print("GRESKA")
    else:
        print(13 - sum(p), 13 - sum(k), 13 - sum(h), 13 - sum(t))

main()
