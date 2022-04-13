

def main():
    # Read input
    s = input()
    # Split input into list of card
    cards = s.split()
    # Initialize dictionary to count number of card of each rank
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
    # Initialize list of ranks with maximum count
    max_count_ranks = []
    # Iterate through ranks
    for rank in rank_count:
        # If rank has maximum count, add to list
        if rank_count[rank] == max_count:
            max_count_ranks.append(rank)
    # Sort list of ranks with maximum count
    max_count_ranks.sort()
    # Output maximum count
    print(max_count_ranks[0])

if __name__ == "__main__":
    main()
