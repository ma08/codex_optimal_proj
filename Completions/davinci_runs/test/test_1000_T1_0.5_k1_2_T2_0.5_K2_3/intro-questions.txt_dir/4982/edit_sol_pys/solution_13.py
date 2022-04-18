
    import sys
def main():
    # Read input
    events = []
    for line in sys.stdin:
        events.append(line.strip().split())

    # Initialise variables
    num_shares = 0
    total_cost = 0
    total_sale = 0
    num_sold = 0
    tax_rate = 0.3

    # Process events 
    for event in events:
        if event[0] == 'buy':
            num_shares += int(event[1])
            total_cost += int(event[1]) * int(event[2])
        elif event[0] == 'sell':
            num_shares -= int(event[1])
            total_sale += (int(event[1]) * int(event[2]))
            num_sold += int(event[1])
        elif event[0] == 'split':
            num_shares *= int(event[1])
            total_cost = total_cost * int(event[1])
        elif event[0] == 'merge':
            num_shares = num_shares // int(event[1])
            total_cost = total_cost // int(event[1])
        elif event[0] == 'die':
            total_sale += int(event[1]) * (num_shares - num_sold)
            total_sale -= total_sale * tax_rate
            break

    print(total_sale)

if __name__ == "__main__":
    main()
