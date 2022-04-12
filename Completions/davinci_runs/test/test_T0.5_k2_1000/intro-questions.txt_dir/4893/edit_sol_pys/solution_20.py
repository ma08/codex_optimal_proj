
def main():
    n, p = [int(x) for x in input().split()]  # n is the number of houses and p is the number of people
    distances = [int(x) for x in input().split()]  # distances is the list of distances between houses

    distances.sort()
    min_distance = distances[1] - distances[0]  # min_distance is the minimum distance between houses

    for i in range(1, n):
        if distances[i] - distances[i - 1] < min_distance:
            min_distance = distances[i] - distances[i - 1]

    print(min_distance)

if __name__ == '__main__':
    main()
