import math

def calculate_fuel(mass):
    fuel = math.floor(int(mass) / 3) - 2
    return fuel

with open('input.txt', 'r') as f:
    masses = f.readlines()

total_fuel = 0

for mass in masses:
    total_fuel += calculate_fuel(mass)

print(total_fuel)
