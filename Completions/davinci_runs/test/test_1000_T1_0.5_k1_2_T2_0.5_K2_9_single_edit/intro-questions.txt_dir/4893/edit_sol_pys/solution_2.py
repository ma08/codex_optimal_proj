

#========================================================================
#=============================CODE=======================================
#========================================================================
import math


    #Read input
import sys

def main():
    input = sys.stdin.readline().split()
    n = int(input[0]) #Number of houses
    p = int(input[1]) #Number of pipes
    input = sys.stdin.readline().split()
    houses = [int(i) for i in input]
    houses.sort()
    #print(houses)

    #Find min distance between houses
    min_dist = houses[1] - houses[0]
    for i in range(2, n):
        if houses[i] - houses[i-1] < min_dist:
            min_dist = houses[i] - houses[i-1]

    #Find max distance between houses
    max_dist = houses[n-1] - houses[0]

    #Binary search for max number of pipes
    #max_pipes = math.floor(max_dist / min_dist)
    #min_pipes = 1
    #curr_pipes = (min_pipes + max_pipes)//2
    #print(min_pipes, max_pipes, curr_pipes)

    #while max_pipes - min_pipes > 1:
    #    print(min_pipes, max_pipes, curr_pipes)
    #    if is_possible(houses, curr_pipes, min_dist):
    #        min_pipes = curr_pipes
    #    else:
    #        max_pipes = curr_pipes
    #    curr_pipes = (min_pipes + max_pipes)//2
    #print(min_pipes, max_pipes, curr_pipes)

    #if is_possible(houses, max_pipes, min_dist):
    #    print(max_pipes)
    #else:
    #    print(min_pipes)

def is_possible(houses, pipes, min_dist):
    if pipes == 1:
        return True
    curr_dist = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - curr_dist >= min_dist:
            curr_dist = houses[i]
            pipes -= 1
            if pipes == 1:
                return True
    return False

main()
