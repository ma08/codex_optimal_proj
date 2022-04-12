import sys



def main():
    # Read input
    events = []
    for line in sys.stdin:
        events.append(line.strip().split())

    # Initialize variables
    num_shares = 0  # Number of shares
    total_cost = 0  # Total cost of shares
    total_sale = 0  # Total sale of shares
    num_sold = 0  # Number of shares sold
    avg_cost = 0  # Average cost of shares
    avg_sale = 0  # Average sale of shares
    tax_rate = 0.3

    # Process events
    for event in events:
        if event[0] == 'buy':
            num_shares += int(event[1])
            total_cost += int(event[1]) * int(event[2])
        elif event[0] == 'sell':
            num_shares -= int(event[1])
            avg_sale = (int(event[1]) * int(event[2])) / int(event[1])
            total_sale += avg_sale * int(event[1])
            num_sold += int(event[1])
        elif event[0] == 'split':
            num_shares *= int(event[1])
            total_cost = total_cost * int(event[1])
        elif event[0] == 'merge':
            num_shares = num_shares // int(event[1])
            total_cost = total_cost // int(event[1])
        elif event[0] == 'die':
            avg_cost = total_cost / num_shares
            avg_sale = int(event[1])
            total_sale += avg_sale * (num_shares - num_sold)
            total_sale -= total_sale * tax_rate
            break

    print(total_sale)

if __name__ == "__main__":
    main()
