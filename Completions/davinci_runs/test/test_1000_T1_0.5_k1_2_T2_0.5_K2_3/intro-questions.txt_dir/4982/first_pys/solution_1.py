

from sys import stdin

def main():
    events = []
    for line in stdin:
        events.append(line.strip().split())
    total = 0
    numShares = 0
    for event in events:
        if event[0] == "buy":
            numShares += int(event[1])
            total += int(event[1]) * int(event[2])
        if event[0] == "sell":
            numShares -= int(event[1])
            total -= int(event[1]) * int(event[2])
        if event[0] == "split":
            numShares *= int(event[1])
            total *= int(event[1])
        if event[0] == "merge":
            numShares //= int(event[1])
            total //= int(event[1])
            if numShares % int(event[1]):
                numShares -= numShares % int(event[1])
                total -= total % int(event[1])
        if event[0] == "die":
            total -= total * 0.3
            total += numShares * int(event[1])
    print(format(total, ".8f"))

if __name__ == "__main__":
    main()