

def main():
    n, p = [int(x) for x in input().split()]
    distances = [int(x) for x in input().split()]

    distances.sort()
    min_distance = distances[0]
    for i in range(1, n):
        if distances[i] - distances[i - 1] < min_distance:
            min_distance = distances[i] - distances[i - 1]

    print(min_distance)

if __name__ == '__main__':
    main()