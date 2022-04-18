

import sys
import math

def readline():
    return sys.stdin.readline().strip()

def main():
    R, S = [int(x) for x in readline().split()]
    seats = []
    for _ in range(R):
        seats.append(list(readline()))
    #print(seats)
    #print(R, S)
    #print(seats[0][0])
    #print(seats[0][1])
    #print(seats[1][0])
    #print(seats[1][1])
    #print(seats[0][2])
    #print(seats[1][2])
    #print(seats[0][3])
    #print(seats[1][3])
    #print(seats[2][0])
    #print(seats[2][1])
    #print(seats[2][2])
    #print(seats[2][3])
    #print(seats[3][0])
    #print(seats[3][1])
    #print(seats[3][2])
    #print(seats[3][3])
    #print(seats[0][4])
    #print(seats[1][4])
    #print(seats[2][4])
    #print(seats[3][4])
    #print(seats[0][5])
    #print(seats[1][5])
    #print(seats[2][5])
    #print(seats[3][5])

    handshakes = 0
    for x in range(R):
        for y in range(S):
            #print(x, y)
            if seats[x][y] == "o":
                #print("o")
                if x > 0:
                    if y > 0:
                        if seats[x-1][y-1] == "o":
                            handshakes += 1
                    if seats[x-1][y] == "o":
                        handshakes += 1
                    if y+1 < S:
                        if seats[x-1][y+1] == "o":
                            handshakes += 1
                if y > 0:
                    if seats[x][y-1] == "o":
                        handshakes += 1
                if y+1 < S:
                    if seats[x][y+1] == "o":
                        handshakes += 1
                if x+1 < R:
                    if y > 0:
                        if seats[x+1][y-1] == "o":
                            handshakes += 1
                    if seats[x+1][y] == "o":
                        handshakes += 1
                    if y+1 < S:
                        if seats[x+1][y+1] == "o":
                            handshakes += 1
    print(handshakes)

if __name__ == "__main__":
    main()