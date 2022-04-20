

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    # First, we must find the total number of passengers and their average
    # for the entire trip.
    total_passengers = sum(a)
    avg_passengers = total_passengers / n

    # The average number of passengers must be between 0 and the bus capacity.
    # If not, then no valid number of passengers at the beginning of the trip
    # exists.
    if not (0 <= avg_passengers <= w):
        print(0)
        return

    # The number of passengers at the beginning of the trip will be equal to
    # the average number of passengers plus or minus the total number of
    # passengers.
    #
    # We know that the number of passengers must be between 0 and the bus
    # capacity.
    #
    # We also know that the number of passengers at the beginning of the trip
    # must be an integer.
    #
    # Therefore, the number of passengers at the beginning of the trip will be
    # equal to the floor of the average number of passengers plus the total
    # number of passengers or the ceiling of the average number of passengers
    # minus the total number of passengers.
    #
    # We must check if each of these values is between 0 and the bus capacity
    # and if they are integers.
    #
    # If they are, then the number of passengers at the beginning of the trip
    # will be one of these values.
    #
    # If one or both of these values is not an integer or not between 0 and
    # the bus capacity, then the number of passengers at the beginning of the
    # trip will be the other value.
    #
    # If both values are not integers or not between 0 and the bus capacity,
    # then no valid number of passengers at the beginning of the trip exists.

    start_passengers = int(avg_passengers + total_passengers)
    end_passengers = int(avg_passengers - total_passengers)

    if (0 <= start_passengers <= w) and (0 <= end_passengers <= w):
        print(2)
    elif (0 <= start_passengers <= w) or (0 <= end_passengers <= w):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()