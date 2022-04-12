

from sys import stdin

def main():
    events = []
    for line in stdin:
        events.append(line.strip().split())
    total = 0
    numShares = 0
    for event in events:
        if event[0] == "buy": # buy shares
            numShares += int(event[1])
            total += int(event[1]) * int(event[2])
        if event[0] == "sell": # sell shares
            numShares -= int(event[1])
            total -= int(event[1]) * int(event[2])
        if event[0] == "split": # split shares
            numShares *= int(event[1])
            total *= int(event[1])
        if event[0] == "merge": # merge shares
            numShares //= int(event[1])
            total //= int(event[1])
            if numShares % int(event[1]):
                numShares -= numShares % int(event[1])
                total -= total % int(event[1])
        if event[0] == "die": # die
            total -= total * 0.3 # 30% tax
            total += numShares * int(event[1])
    print(format(total, ".8f"))

if __name__ == "__main__":
    main()
