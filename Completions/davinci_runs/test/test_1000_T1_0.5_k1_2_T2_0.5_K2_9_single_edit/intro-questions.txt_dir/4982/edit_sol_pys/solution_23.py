
import sys

def main():
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    num_shares = 0
    cost_per_share = 0
    for line in lines:
        event = line.split()
        if event[0] == 'buy':
            num_shares += int(event[1])
            cost_per_share += int(event[1]) * int(event[2])
        elif event[0] == 'sell':
            num_shares -= int(event[1])
            cost_per_share -= int(event[1]) * int(event[2])
        elif event[0] == 'split':
            num_shares *= int(event[1])
            cost_per_share /= int(event[1])
        elif event[0] == 'merge':
            num_shares_to_merge = num_shares - (num_shares % int(event[1]))
            num_shares -= num_shares_to_merge
            cost_per_share = (cost_per_share * num_shares_to_merge) / int(event[1])
            num_shares += 1
        elif event[0] == 'die':
            final_sum = num_shares * (int(event[1]) - (0.3 * (int(event[1]) - cost_per_share / num_shares)))
            print(final_sum)
if __name__ == '__main__':
    main()
