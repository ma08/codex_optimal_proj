

#Program:

def generate_taxi_numbers(m):
    taxi = set()
    for i in range(1, int(m**0.5)+1):
        for j in range(i, int(m**0.5)+1):
            n = i**3 + j**3
            if n < m:
                taxi.add(n)
    return taxi


def generate_bus_numbers(taxi_numbers):
    bus_numbers = set()
    for n in taxi_numbers:
        if taxi_numbers.count(n) > 1:
            bus_numbers.add(n)
    return bus_numbers


def main():
    m = int(input())
    taxi_numbers = generate_taxi_numbers(m)
    bus_numbers = generate_bus_numbers(taxi_numbers)
    if len(bus_numbers) > 0:
        print(max(bus_numbers))
    else:
        print("none")


if __name__ == "__main__":
    main()
