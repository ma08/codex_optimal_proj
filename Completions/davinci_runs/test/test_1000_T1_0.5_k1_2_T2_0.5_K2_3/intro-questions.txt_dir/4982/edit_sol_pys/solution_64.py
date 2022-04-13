
import sys

def main():
    events = []
    for line in sys.stdin:
        args = line.split()
        events.append(args)

    shares_owned = 0
    share_cost = 0.0
    for event in events:
        if event[0] == "buy":
            shares_owned += int(event[1])
            share_cost = (share_cost * (shares_owned - int(event[1])) + float(event[1]) * float(event[2])) / shares_owned
        elif event[0] == "sell":
            shares_owned -= int(event[1])
        elif event[0] == "split":
            shares_owned *= int(event[1])
            share_cost /= int(event[1])
        elif event[0] == "merge": #merge is the same as a reverse split
            shares_owned = (shares_owned // int(event[1])) + (shares_owned % int(event[1]))
            share_cost *= int(event[1])
        elif event[0] == "die":
            share_cost = float(event[1])
            break

    print(shares_owned * share_cost * (1 - 0.3))

main()
