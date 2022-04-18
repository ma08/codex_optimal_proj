
#Program: Taxi and Bus numbers

m = int(input())

def generate_taxi_numbers(m):
    taxi = []
    for i in range(1, int(m**0.5)+1):
        for j in range(i, int(m**0.5)+1):
            if i != j:
                n = i**3 + j**3
                if n < m:
                    taxi.append(n)
    return taxi
taxi_numbers = generate_taxi_numbers(m)

bus_numbers = []
for n in taxi_numbers:
    if taxi_numbers.count(n) > 1:
        bus_numbers.append(n)

if len(bus_numbers) > 0:
    print(max(bus_numbers))
else:
    print("none")
