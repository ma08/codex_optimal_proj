

#Program: Taxi Bus Numbers

import math

def taxi_numbers(m):
    taxi_numbers = []
    for i in range(1, int(math.sqrt(m)+1)):
        for j in range(i, int(math.sqrt(m)+1)):
            if i != j and i**3 + j**3 < m:
                taxi_numbers.append(i**3 + j**3)
    return taxi_numbers

def bus_numbers(m):
    bus_numbers = []
    for n in taxi_numbers(m):
        if taxi_numbers(m).count(n) > 1:
            bus_numbers.append(n)
    return bus_numbers

def max_bus_number(m):
    if len(bus_numbers(m)) > 0:
        return max(bus_numbers(m))
    else:
        return "none"

print(max_bus_number(int(input())))
