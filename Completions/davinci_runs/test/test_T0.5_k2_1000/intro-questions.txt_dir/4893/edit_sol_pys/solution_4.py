

def main():
    n, p = map(int, input().split())  # n is number of points, p is the distance between points.
    d = [int(x) for x in input().split()]  # d is the list of distances.
    d.sort()  # sort the list.
    min_dist = d[0]  # min_dist is the minimum distance.
    for i in range(1, n):
        if d[i] - d[i - 1] < p * (i + 1):  # if the distance between two points is less than p * (i + 1).
            min_dist = d[i - 1] + p * (i + 1)  # set the min_dist to d[i - 1] + p * (i + 1).
    print(min_dist)

if __name__ == "__main__":
    main()
