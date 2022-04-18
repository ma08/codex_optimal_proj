

def main():
    cards = input()
    cards = cards.split(" ")
    p = 0
    k = 0
    h = 0
    t = 0
    for card in cards:
        if card[0] == "P":
            p += 1
        elif card[0] == "K":
            k += 1
        elif card[0] == "H":
            h += 1
        elif card[0] == "T":
    if p > 13 or k > 13 or h > 13 or t > 13:
        print("GRESKA")
    else:
        print(13 - p, 13 - k, 13 - h, 13 - t)

main()
