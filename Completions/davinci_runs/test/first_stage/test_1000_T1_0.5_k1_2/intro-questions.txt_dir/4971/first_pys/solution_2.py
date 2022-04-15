

import sys

def main():
    m = int(sys.stdin.readline())
    bus_numbers = set()
    cubes = set()
    cube_sums = set()
    i = 1
    while True:
        cube = i**3
        cubes.add(cube)
        new_sums = set(map(lambda x: x + cube, cube_sums))
        for s in new_sums:
            if s in cubes:
                bus_numbers.add(s)
        cube_sums = cube_sums.union(new_sums)
        if cube > m:
            break
        i += 1
    bus_numbers = list(bus_numbers)
    bus_numbers.sort()
    if bus_numbers[-1] <= m:
        print(bus_numbers[-1])
    else:
        print("none")
        
if __name__ == "__main__":
    main()