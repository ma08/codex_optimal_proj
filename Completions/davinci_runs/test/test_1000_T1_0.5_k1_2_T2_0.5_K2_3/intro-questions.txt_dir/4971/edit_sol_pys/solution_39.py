

import sys

def main():
    m = int(sys.stdin.readline())
    bus_numbers = []
    cubes = []
    cube_sums = []
    i = 1
    while True:
        cube = i**3
        cubes.append(cube)
        new_sums = list(map(lambda x: x + cube, cube_sums))
        for s in new_sums:
            if s in cubes:
                bus_numbers.append(s)
        cube_sums = cube_sums + new_sums
        if cube > m:
            break
        i += 1
    bus_numbers.sort()
    print(bus_numbers)
    if len(bus_numbers) > 0 and bus_numbers[-1] <= m:
        print(bus_numbers[-1])
    else:
        print("none")
        
if __name__ == "__main__":
    main()
