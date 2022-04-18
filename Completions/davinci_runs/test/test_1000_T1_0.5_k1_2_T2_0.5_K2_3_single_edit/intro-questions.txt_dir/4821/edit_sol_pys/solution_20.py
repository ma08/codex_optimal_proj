

def main():
    cards = input()
    cards = cards.split(" ")
    p = [0] * 14
    k = [0] * 14
    h = [0] * 14
    t = [0] * 14
    for card in cards:
        if card[0] == "P":
            p[int(card[1:])] += 1
        elif card[0] == "K":
            k[int(card[1:])] += 1
        elif card[0] == "H":
            h[int(card[1:])] += 1
        elif card[0] == "T":
            t[int(card[1:])] += 1
    if max(p) > 1 or max(k) > 1 or max(h) > 1 or max(t) > 1:
        print("GRESKA")
    else:
        print(13 - sum(p[1:]), 13 - sum(k[1:]), 13 - sum(h[1:]), 13 - sum(t[1:]))

main()
