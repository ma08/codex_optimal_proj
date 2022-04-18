import math

import sys

def get_fuel(mass):
    return math.floor(mass/3) - 2

def get_fuel_for_fuel(mass):
    fuel = 0
    extra_fuel = get_fuel(mass)
    while extra_fuel > 0:
        fuel += extra_fuel
        extra_fuel = get_fuel(extra_fuel)
    return fuel

def main():
    lines = [line.strip() for line in sys.stdin]
    total_fuel = 0
    for line in lines:
        total_fuel += get_fuel(int(line))
        total_fuel += get_fuel_for_fuel(int(line))
    print(total_fuel)

if __name__ == "__main__":
    main()
