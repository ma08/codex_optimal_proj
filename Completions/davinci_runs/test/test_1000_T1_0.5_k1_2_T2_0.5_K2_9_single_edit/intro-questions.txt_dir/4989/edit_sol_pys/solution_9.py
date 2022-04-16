#!/usr/bin/env python3

n = int(input())
pieces = [int(x) for x in input().split()]

def play(n, pieces, turn):
    if turn:
        if n == 1:
            return pieces[0], 0
        elif n == 2:
            return max(pieces[0], pieces[1]), min(pieces[0], pieces[1])
        else:
            if pieces[0] > pieces[-1]:
                a, b = play(n-1, pieces[1:], False)
                return pieces[0] + b, a
            else:
                a, b = play(n-1, pieces[:-1], False)
                return a, pieces[-1] + b
    else: 
        if n == 1:
            return 0, pieces[0]
        elif n == 2:
            return max(pieces[0], pieces[1]), min(pieces[0], pieces[1])
        else:
            if pieces[0] > pieces[-1]:
                a, b = play(n-1, pieces[1:], True)
                return pieces[0] + b, a
            else:
                a, b = play(n-1, pieces[:-1], True)
                return a, pieces[-1] + b

a, b = play(n, pieces)
print(a, b)
