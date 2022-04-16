

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()] # n = number of cows, m = number of barns
    times = [[int(i) for i in sys.stdin.readline().split()] for i in range(n)] # times[i][j] = time it takes cow i to get to barn j
    swathers = [[i,j] for i in range(n) for j in range(m)] # swathers = list of cows and barns
    swathers = sorted(swathers, key=lambda x: times[x[0]][x[1]]) # sort swathers by time it takes cow to get to barn
    completed = [0]*n # completed = list of times it takes each cow to get to its barn
    while len(swathers) > 0: # while there are still cows and barns
        swather = swathers.pop(0) # swather = the next cow and barn
        if swather[1] == 0: # if the swather is at the first barn
            completed[swather[0]] = times[swather[0]][0] # the cow is done when it gets to the first barn
        else: # if the swather is not at the first barn
            completed[swather[0]] = max(completed[swather[0]], completed[swather[0]-1]) + times[swather[0]][swather[1]] # the cow is done when it gets to the barn or when the previous cow gets to the barn, whichever is later
    print(' '.join([str(i) for i in completed])) # print the times it takes each cow to get to its barn

if __name__ == '__main__':
    main()
