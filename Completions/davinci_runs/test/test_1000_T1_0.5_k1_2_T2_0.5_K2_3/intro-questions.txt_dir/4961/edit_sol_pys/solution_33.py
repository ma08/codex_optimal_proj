

import sys
import math

def readline():
    return sys.stdin.readline().strip()

def main():
    R, S = [int(x) for x in readline().split()] # read R,S
    seats = []
    for _ in range(R):
        seats.append(list(readline())) # read seats
    #print(seats)
    #print(R, S)

    handshakes = 0
    for x in range(R):
        for y in range(S):
            #print(x, y)
            if seats[x][y] == "o": # if seat is occupied
                #print("o")
                if x > 0:
                    if y > 0:
                        if seats[x-1][y-1] == "o": # if left-up seat is occupied
                            handshakes += 1
                    if seats[x-1][y] == "o": # if up seat is occupied
                        handshakes += 1
                    if y+1 < S:
                        if seats[x-1][y+1] == "o": # if right-up seat is occupied
                            handshakes += 1
                if y > 0:
                    if seats[x][y-1] == "o": # if left seat is occupied
                        handshakes += 1
                if y+1 < S:
                    if seats[x][y+1] == "o": # if right seat is occupied
                        handshakes += 1
                if x+1 < R:
                    if y > 0:
                        if seats[x+1][y-1] == "o": # if left-down seat is occupied
                            handshakes += 1
                    if seats[x+1][y] == "o": # if down seat is occupied
                        handshakes += 1
                    if y+1 < S:
                        if seats[x+1][y+1] == "o": # if right-down seat is occupied
                            handshakes += 1
    print(handshakes)

if __name__ == "__main__":
    main()
