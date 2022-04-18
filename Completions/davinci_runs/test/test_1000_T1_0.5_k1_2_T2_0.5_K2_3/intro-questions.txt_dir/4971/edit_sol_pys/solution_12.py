
import sys

def is_cube(n):
    return round(n**(1./3.)) ** 3 == n

def find_cubes(max_n):
    cubes = []
    for i in range(1, max_n+1):
        if is_cube(i):
            cubes.append(i)
    return cubes

def find_bus_numbers(m): 
    cubes = find_cubes(m)
    numbers = {}
    for c1 in cubes:
        for c2 in cubes:
            if c1 + c2 <= m:
                if c1 + c2 in numbers:
                    numbers[c1 + c2] += 1
                else:
                    numbers[c1 + c2] = 1
    return numbers

def find_max_bus_number(numbers):
    max_bus_number = 0
    for number in numbers:
        if numbers[number] >= 2 and number > max_bus_number:
            max_bus_number = number
    return max_bus_number

def main():
    m = int(sys.stdin.readline().strip())
    numbers = find_bus_numbers(m)
    max_bus_number = find_max_bus_number(numbers)
    if max_bus_number == 0:
        print("none")
    else:
        print(max_bus_number)

if __name__ == "__main__":
    main()
