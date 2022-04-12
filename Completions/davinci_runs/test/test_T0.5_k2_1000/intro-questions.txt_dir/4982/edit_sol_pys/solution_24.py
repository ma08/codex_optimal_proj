

def main():
    events = []
    while True:
        event = input().split()
        if event[0] == "die":  # end of input
            events.append(event)
            break
        else:  # add event to list
            events.append(event)

    stock = 0  # stock number
    cost = 0  # average cost
    for event in events:
        if event[0] == "buy":  # buy stock
            stock += int(event[1])
            cost += int(event[1]) * int(event[2])
        elif event[0] == "sell":  # sell stock
            stock -= int(event[1])
            cost -= int(event[1]) * int(event[2])
        elif event[0] == "split":
            stock *= int(event[1])
            cost /= int(event[1])
        elif event[0] == "merge":
            stock = stock // int(event[1])
            cost = cost * int(event[1])
        elif event[0] == "die":
            print("{:.8f}".format(stock * int(event[1]) - stock * cost * 0.3))  # print result

if __name__ == "__main__":
    main()
