

def main():
    # Read input and split into list of cards
    cards = input().split()
    # Get count of card ranks
    rank_count = get_rank_count(cards)
    # Get maximum rank count
    max_count = get_max_count(rank_count)
    # Output maximum rank count
    print(max_count, end="")

def get_rank_count(cards):
    # Initialize rank count dictionary
    rank_count = dict()
    # Iterate through cards and increment rank count
    for card in cards: rank_count[card[0]] = rank_count.get(card[0], 0) + 1
    # Return rank count dictionary
    return rank_count

def get_max_count(rank_count):
    # Initialize maximum count
    max_count = 0
    # Iterate through rank count dictionary and find maximum count
    for rank in rank_count: max_count = max(max_count, rank_count[rank])
    # Return maximum count
    return max_count

if __name__ == "__main__":
    main()
