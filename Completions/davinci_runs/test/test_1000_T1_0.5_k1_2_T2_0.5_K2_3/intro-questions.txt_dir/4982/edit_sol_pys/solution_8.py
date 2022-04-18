

def main():
    events = []
    while True:
        event = input().split()
        if event[0] == "die":
            events.append(event)
            break
        else:
            events.append(event)

    stock = 0
    costs = 0
    for event in events:
        if event[0] == "buy":
            stock += int(event[1])
            costs += int(event[1]) * int(event[2])
        elif event[0] == "sell":
            stock -= int(event[1])
            costs -= int(event[1]) * int(event[2])
        elif event[0] == "split":
            stock *= int(event[1])
            costs /= int(event[1])
        elif event[0] == "merge":
            stock = stock // int(event[1])
            costs = costs * int(event[1])
        elif event[0] == "die":
            print("{:.8f}".format(stock * int(event[1]) - stock * costs * 0.3)

if __name__ == "__main__":
    main()
