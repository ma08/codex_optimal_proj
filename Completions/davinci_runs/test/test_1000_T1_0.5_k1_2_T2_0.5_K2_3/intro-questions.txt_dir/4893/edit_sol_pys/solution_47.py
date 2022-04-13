

def main():
    n = int(input())
    distances = [int(x) for x in input().split()]

    distances.sort()
    min_distance = distances[0]
    for i in range(1, n - 1):
        if distances[i + 1] - distances[i] < min_distance:
            min_distance = distances[i + 1] - distances[i]

    print(min_distance)

if __name__ == '__main__':
    main()
