

def get_hand_strength(hand): 
    ranks = [card[0] for card in hand.split()]
    return max([ranks.count(rank) for rank in ranks])

def main():
    hand = input()
    print(get_hand_strength(hand))

main()
