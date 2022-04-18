

def get_hand_strength(hand, community_cards):
    # ranks = [card[0] for card in hand]
    # return max([ranks.count(rank) for rank in ranks])
    hand_cards = hand + community_cards
    print(hand_cards)

def get_community_cards(community_cards):
    return community_cards.split()

def main():
    hand = input().split()
    community_cards = input()
    print(get_hand_strength(hand, get_community_cards(community_cards)))

main()
