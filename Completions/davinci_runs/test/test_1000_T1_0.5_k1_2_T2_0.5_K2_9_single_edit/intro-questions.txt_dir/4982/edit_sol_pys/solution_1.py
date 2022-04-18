

import sys

def main():
    # Reading in the input
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    # Initializing variables
    num_shares = 0
    cost_per_share = 0
    # Iterating through the events
    for line in lines:
        event = line.split()
        # Buy event
        if event[0] == 'buy':
            num_shares += int(event[1])
            cost_per_share += int(event[1]) * float(event[2])
        # Sell event
        elif event[0] == 'sell':
            num_shares -= int(event[1])
            cost_per_share -= int(event[1]) * float(event[2])
        # Split event
        elif event[0] == 'split':
            num_shares *= int(event[1])
            cost_per_share /= int(event[1])
        # Merge event
        elif event[0] == 'merge':
            # Calculate how many shares will be merged
            num_shares_to_merge = num_shares - (num_shares % int(event[1]))
            num_shares -= num_shares_to_merge
            cost_per_share = (cost_per_share * num_shares_to_merge) / float(event[1])
            num_shares += 1
        # Die event
        elif event[0] == 'die':
            # Calculate the final sum after taxes
            final_sum = num_shares * (float(event[1]) - (0.3 * (float(event[1]) - cost_per_share / num_shares)))
            print(final_sum)

if __name__ == '__main__':
    main()
