

def main():
    # Read input
    s = raw_input()
    # Split input into list of cards
    cards = s.split()
    # Initialize dictionary to count number of cards of each rank
    rank_count = {}
    # Iterate through cards
    for card in cards:
        # Get rank of current card
        rank = card[0]
        # If there are no cards of this rank, initialize count to 1
        if rank not in rank_count:
            rank_count[rank] = 1
        # If there are cards of this rank, increment count
        else:
            rank_count[rank] += 1
    # Get maximum count
    max_count = max(rank_count.values())
    # Output maximum count
    print(max_count)

if __name__ == "__main__":
    main()
