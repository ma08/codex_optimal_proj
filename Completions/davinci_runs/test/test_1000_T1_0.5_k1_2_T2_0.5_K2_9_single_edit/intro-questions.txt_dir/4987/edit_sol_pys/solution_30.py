

def calculate_min_stops(distance, tank_size, gas_stations):
    gas_stations.append(distance)
    gas_stations = [0] + gas_stations
    current_position = 0
    stops = 0
    while current_position < len(gas_stations) - 1:
        last_position = current_position
        while (current_position < len(gas_stations) - 1 and
               gas_stations[current_position + 1] - gas_stations[last_position] <= tank_size):
            current_position += 1
        if current_position == last_position:
            return -1
        if current_position < len(gas_stations) - 1:
            stops += 1
    return stops


if __name__ == '__main__':
    distance, tank_size, num_stations = map(int, input().split())
    gas_stations = list(map(int, input().split()))

    print(calculate_min_stops(distance, tank_size, gas_stations))
