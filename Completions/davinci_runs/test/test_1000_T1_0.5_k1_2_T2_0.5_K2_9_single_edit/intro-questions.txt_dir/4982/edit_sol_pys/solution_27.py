

def main():
    events = []
    while True:
        event = input().split()
        if event[0] == "die" or event[0] == "DIE":
            events.append(event)
            break
        else:
            events.append(event)

    stock = 0
    cost = 0
    for event in events:
        if event[0] == "buy" or event[0] == "BUY":
            stock += int(event[1])
            cost += int(event[1]) * int(event[2])
        elif event[0] == "sell" or event[0] == "SELL":
            stock -= int(event[1])
            cost -= int(event[1]) * int(event[2])
        elif event[0] == "split" or event[0] == "SPLIT":
            stock *= int(event[1])
            cost /= int(event[1])
        elif event[0] == "merge" or event[0] == "MERGE":
            stock = stock // int(event[1])
            cost = cost * int(event[1])
        elif event[0] == "die" or event[0] == "DIE":
            print("{:.8f}".format(stock * int(event[1]) - stock * cost * 0.3))

if __name__ == "__main__":
    main()
