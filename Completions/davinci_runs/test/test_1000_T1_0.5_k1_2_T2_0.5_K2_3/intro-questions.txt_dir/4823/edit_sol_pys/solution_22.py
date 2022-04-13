

def get_hand_strength(hand): 
    ranks = [card[0] for card in hand] # list of ranks in hand
    return max([ranks.count(rank) for rank in ranks]) # return max number of cards of same rank

def main():
    hand = input().split() # input hand
    print(get_hand_strength(hand)) # print result

main() # run program
