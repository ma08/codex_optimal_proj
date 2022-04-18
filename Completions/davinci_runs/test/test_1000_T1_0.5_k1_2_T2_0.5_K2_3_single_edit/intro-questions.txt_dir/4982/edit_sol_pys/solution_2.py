

import sys

def main():
    events = [] # list of events
    for line in sys.stdin:
        args = line.split() # split the line into a list
        events.append(args) # add the event to the list of events

    shares_owned = 0 # number of shares owned
    share_cost = 0.0 # cost of a share
    for event in events:
        if event[0] == "buy":
            shares_owned += int(event[1]) # add to shares_owned
            share_cost = (share_cost * (shares_owned - int(event[1])) + int(event[1]) * float(event[2])) / shares_owned # update share_cost
        elif event[0] == "sell":
            shares_owned -= int(event[1]) # subtract from shares_owned
        elif event[0] == "split":
            shares_owned *= int(event[1]) # multiply shares_owned
            share_cost /= int(event[1]) # divide share_cost
        elif event[0] == "merge":
            shares_owned = (shares_owned // int(event[1])) + (shares_owned % int(event[1])) # divide shares_owned
            share_cost *= int(event[1]) # multiply share_cost
        elif event[0] == "die":
            share_cost = float(event[1]) # update share_cost
            break

    print(shares_owned * share_cost * (1 - 0.3)) # print the result

main()
