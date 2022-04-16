#==================================================================
#===========================LIBRARIES==============================
#==================================================================

import sys

#==================================================================
#=======================GLOBAL VARIABLES===========================
#==================================================================



#==================================================================
#===========================FUNCTIONS==============================
#==================================================================

def main():
    input = sys.stdin.readline().split()
    n = int(input[0])
    p = int(input[1])
    input = sys.stdin.readline().split()
    cars = [int(i) for i in input]
    cars.sort()
    #print(cars)
    min_dist = cars[0]
    for i in range(1, n):
        if cars[i] - cars[i-1] < min_dist:
            min_dist = cars[i] - cars[i-1]
    print(min_dist)

#==================================================================
#=============================CODE=================================
#==================================================================

main()

#==================================================================
#=============================CODE=================================
#==================================================================


#==================================================================
#===========================LIBRARIES==============================
#==================================================================

import sys, math

#==================================================================
#=======================GLOBAL VARIABLES===========================
#==================================================================



#==================================================================
#===========================FUNCTIONS==============================
#==================================================================

def main():
    input = sys.stdin.readline().split()
    n = int(input[0])
    w = int(input[1])
    l = int(input[2])
    r = int(input[3])
    input = sys.stdin.readline().split()
    radii = [int(i) for i in input]
    radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x > r]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x <= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x >= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x <= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x >= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x <= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x >= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x <= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x >= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x <= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x <= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #radii = [x for x in radii if x >= r]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= w/2]
    #radii.sort()
    #print(radii)
    #radii = [x for x in radii if x >= l/2]
    #radii.sort()
    #print(radii)
    #print(radii)
    #print(radii)
    #print(radii)
    #print(radii)
    #print(radii)
    #print(radii)
    #print(radii)

#==================================================================
#=============================CODE=================================
#==================================================================

main()
