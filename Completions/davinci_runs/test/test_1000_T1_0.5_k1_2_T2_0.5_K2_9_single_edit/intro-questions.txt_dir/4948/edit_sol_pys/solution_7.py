

import sys
import math

def get_weight(radius, thickness):
    return 4/3 * math.pi * radius**3 - 4/3 * math.pi * (radius - thickness)**3

def get_slice_thickness(radius, weight):
    return math.pow(3 * (math.pow(radius, 3) - math.pow(radius - weight, 3)) / (4 * math.pi), 1/3)

def main():
    line = sys.stdin.readline().split()
    holes = int(line[0]) #number of holes
    slices = int(line[1]) #number of slices
    weights = []
    total_weight = 0
    for i in range(holes):
        line = sys.stdin.readline().split()
        radius = int(line[0]) #radius of hole
        x = int(line[1]) #x coordinate of hole
        y = int(line[2]) #y coordinate of hole
        z = int(line[3]) #z coordinate of hole
        weight = get_weight(radius, 100)
        weights.append(weight)
        total_weight += weight
    weights.sort()
    weights.reverse()
    weights.append(0)
    slice_weight = total_weight / slices #weight of each slice
    weight_so_far = 0
    weight_remaining = slice_weight #weight left to fill in each slice
    weights_used = []
    for i in range(slices):
        if weights_used:
            weight_remaining = slice_weight - weight_so_far #reset weight remaining
        for j in range(len(weights)):
            #add the largest weight that will fit in the slice
            if weights[j] <= weight_remaining:
                weight_remaining -= weights[j] #reduce weight remaining
                weight_so_far += weights[j] #increment weight so far
                weights_used.append(weights[j]) #add weight to weights used
                break
    #print the thicknesses of each slice
    for weight in weights_used:
        print(get_slice_thickness(50, weight))

if __name__ == "__main__":
    main()
