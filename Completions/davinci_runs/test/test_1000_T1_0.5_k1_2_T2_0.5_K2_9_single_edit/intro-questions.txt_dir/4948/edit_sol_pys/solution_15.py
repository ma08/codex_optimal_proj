

import sys
import math

def get_weight(radius, thickness):
    return 4/3 * math.pi * radius**3 - 4/3 * math.pi * (radius - thickness)**3

def get_slice_thickness(radius, weight):
    return math.pow(3 * (math.pow(radius, 3) - math.pow(radius - weight, 3)) / (4 * math.pi), 1/3)

def main():
    line = sys.stdin.readline().split()
    holes = int(line[0])
    slices = int(line[1])
    weights = []
    total_weight = 0
    for i in range(holes):
        line = sys.stdin.readline().split()
        radius = int(line[0])
        x = int(line[1])
        y = int(line[2])
        z = int(line[3])
        weight = get_weight(radius, 100) * 1000
        weights.append(weight)
        total_weight += weight
    weights.sort()
    weights.reverse()
    slice_weight = total_weight / slices
    weight_so_far = 0
    weight_remaining = slice_weight
    weights_used = []
    for i in range(slices):
        if weights_used:
            weight_remaining = slice_weight - weight_so_far
        for j in range(len(weights)):
            if weights[j] <= weight_remaining:
                weight_remaining -= weights[j]
                weight_so_far += weights[j]
                weights_used.append(weights[j])
                break
        weights_used.append(0)
    for weight in weights_used:
        print(get_slice_thickness(50, weight / 1000))

if __name__ == "__main__":
    main()
