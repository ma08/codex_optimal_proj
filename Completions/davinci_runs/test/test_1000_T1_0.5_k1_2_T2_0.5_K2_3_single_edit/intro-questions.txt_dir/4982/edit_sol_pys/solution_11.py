
import sys

def main():
    events = []
    for line in sys.stdin:
        args = line.split()
        events.append(args)

    shares_owned = 0
    share_cost = 0.0
    for event in events:
        if event[0] == "buy": shares_owned += int(event[1])
        elif event[0] == "sell": shares_owned -= int(event[1])
        elif event[0] == "split": shares_owned *= int(event[1])
        elif event[0] == "merge": shares_owned = (shares_owned // int(event[1])) + (shares_owned % int(event[1]))
        elif event[0] == "die": break

        share_cost = (share_cost * (shares_owned - int(event[1])) + int(event[1]) * float(event[2])) / shares_owned

    print(shares_owned * share_cost * (1 - 0.3)) # Brokerage fee of 30%

main()
