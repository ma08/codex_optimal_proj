#! /usr/bin/env python3

n, k = map(int, input().split())  # n = number of cards, k = number of throws
throws = input().split()

position = 0

for i in range(k):
    if throws[i] == 'undo':  # undo the last throw
        position += int(throws[i+1])
    else:  # add the value of the throw to the current position
        position += int(throws[i])
        if position > n-1:  # if the position is out of bounds, bring it back
            position -= n  # can be done with modulo, but this is faster
        elif position < 0:  # if the position is out of bounds, bring it back
            position += n  # can be done with modulo, but this is faster

print(position)
