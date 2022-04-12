

def get_hand_rank(hand):
    ranks = [card[0] for card in hand]
    return max([ranks.count(rank) for rank in set(ranks)])

def main():
    hand = input().split()
    print(get_hand_rank(hand))

main()
