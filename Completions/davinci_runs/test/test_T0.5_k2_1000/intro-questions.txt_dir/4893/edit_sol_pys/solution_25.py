

#==============================================================================
#=============================CODE=============================================
#==============================================================================


import sys

def main():
    input_line = sys.stdin.readline().split()
    n = int(input_line[0])
    p = int(input_line[1])
    input_line = sys.stdin.readline().split()
    cars = [int(i) for i in input_line]
    cars.sort()
    #print(cars)
    min_dist = cars[0]
    for i in range(1, n):
        if cars[i] - cars[i-1] < min_dist:
            min_dist = cars[i] - cars[i-1]
    print(min_dist)

main()
