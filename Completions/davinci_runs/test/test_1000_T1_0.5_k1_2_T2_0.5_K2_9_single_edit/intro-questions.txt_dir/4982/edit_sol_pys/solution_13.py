
import sys

def main():
    for line in sys.stdin:
        event = line.split()

        if event[0] == "buy": 
            shares_owned += int(event[1]) 
            share_cost = (share_cost * (shares_owned - int(event[1])) + int(event[1]) * float(event[2])) / shares_owned 
        elif event[0] == "sell": 
            shares_owned -= int(event[1]) 
        elif event[0] == "split": 
            shares_owned *= int(event[1]) 
            share_cost /= int(event[1]) 
        elif event[0] == "merge": 
            shares_owned = (shares_owned // int(event[1])) + (shares_owned % int(event[1])) 
            share_cost *= int(event[1]) 
        elif event[0] == "die": 
            share_cost = float(event[1]) 
            break 

    print(shares_owned * share_cost * (1 - 0.3))

main()
