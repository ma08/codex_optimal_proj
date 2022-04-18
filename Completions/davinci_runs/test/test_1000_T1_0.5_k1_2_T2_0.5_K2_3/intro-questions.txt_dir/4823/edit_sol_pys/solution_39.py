
def get_hand_strength(hand): 
    ranks = [card[0] for card in hand]
    return max([ranks.count(rank) for rank in ranks])

def main():
    hand = input().split()
    print(get_hand_strength(hand))

if __name__ == "__main__":
    main()
