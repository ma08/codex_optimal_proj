

def main():
    n, p = [int(x) for x in input().split()]  # n is the number of houses and p is the number of people
    distances = [int(x) for x in input().split()]

    distances.sort()  # sort the distances
    min_distance = distances[0]  # initialize the minimum distance
    for i in range(1, n):  # find the minimum distance
        if distances[i] - distances[i - 1] < min_distance:  # check if the difference between the current distance and the previous one is less than the minimum distance
            min_distance = distances[i] - distances[i - 1]  # update the minimum distance

    print(min_distance)

if __name__ == '__main__':
    main()
