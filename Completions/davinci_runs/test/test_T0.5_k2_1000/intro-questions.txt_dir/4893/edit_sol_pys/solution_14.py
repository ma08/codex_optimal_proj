

def main():
    n, p = [int(x) for x in input().split()] # n is number of houses and p is number of pipes
    distances = [int(x) for x in input().split()] # distances between houses

    distances.sort() # sort distances in ascending order
    min_distance = distances[1] - distances[0] # set the minimum distance to the first distance
    for i in range(1, n):
        if distances[i] - distances[i - 1] < min_distance: # if the current distance is less than the minimum distance
            min_distance = distances[i] - distances[i - 1]

    print(min_distance)

if __name__ == '__main__':
    main()
