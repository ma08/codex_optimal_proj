

#===============================================================
#========================CODE===================================
#===============================================================


import sys

def main():
    input = sys.stdin.readline().split()
    n = int(input[0])
    p = int(input[1])
    input = sys.stdin.readline().split()
    cars = [int(i) for i in input]
    cars.sort()
    #print(cars)
    min_dist = cars[1] - cars[0]
    for i in range(1, n):
        if cars[i] - cars[i-1] < min_dist:
            min_dist = cars[i] - cars[i-1]
    print(min_dist)

main()
