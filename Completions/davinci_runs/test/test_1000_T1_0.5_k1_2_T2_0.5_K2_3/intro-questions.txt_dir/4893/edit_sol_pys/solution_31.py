

#==================================================================
#=============================CODE================================
#==================================================================


import sys

def main():
    input_ = sys.stdin.readline().split()
    n = int(input_[0])
    p = int(input_[1])
    input_ = sys.stdin.readline().split()
    cars = [int(i) for i in input_]
    cars.sort()
    #print(cars)
    min_dist = cars[0]
    for i in range(1, n):
        if cars[i] - cars[i-1] < min_dist:
            min_dist = cars[i] - cars[i-1]
    print(min_dist)

main()
