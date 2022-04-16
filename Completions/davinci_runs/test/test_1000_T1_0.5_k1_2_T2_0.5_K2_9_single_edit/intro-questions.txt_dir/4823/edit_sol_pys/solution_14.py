

def get_hand_strength(hand):
    ranks = [card[0] for card in hand] # get all the ranks
    return max([ranks.count(rank) for rank in ranks]) # get the highest count of a rank

def main():
    hand = input().split()
    print(get_hand_strength(hand))

main()
