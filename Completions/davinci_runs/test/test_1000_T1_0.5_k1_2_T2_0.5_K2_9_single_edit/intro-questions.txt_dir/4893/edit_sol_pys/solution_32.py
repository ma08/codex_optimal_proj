

def main():
    n = int(input())
    distances = [int(x) for x in input().split()]

    distances.sort()
    min_distance = distances[1] - distances[0]
    for i in range(2, n):
        if distances[i] - distances[i - 1] < min_distance: min_distance = distances[i] - distances[i - 1]

    print(min_distance)

if __name__ == '__main__':
    main()
