

def get_hand_rank(hand):
    ranks = [card[0] for card in hand] # get the ranks of the hand
    return max([ranks.count(rank) for rank in ranks]) # return the highest count of a rank in the hand

def main():
    hand = input().split() # get the hand from the user
    print(get_hand_rank(hand))

main()
