
import sys
import math

def readline():
    return sys.stdin.readline().strip()

def main():
    R, S = [int(x) for x in readline().split()]
    seats = []
    for _ in range(R):
        seats.append(list(readline()))

    handshakes = 0
    for x in range(R):
        for y in range(S):
            if seats[x][y] == "o":
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
