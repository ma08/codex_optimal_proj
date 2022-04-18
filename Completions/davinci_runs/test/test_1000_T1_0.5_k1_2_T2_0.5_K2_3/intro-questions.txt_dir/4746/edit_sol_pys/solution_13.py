

def main():
    capacity, num_stations = map(int, input().split())
    passengers = [0]
    for i in range(num_stations):
        left, entered, _ = map(int, input().split())
        passengers.append(passengers[-1] + entered - left)
    if passengers[-1] != 0 or max(passengers) > capacity or min(passengers) < 0:
        print("impossible") 
    else:
        print("possible")

if __name__ == '__main__':
    main()
