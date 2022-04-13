# https://www.codechef.com/problems/MARCHA1


def main():
    n, p = [int(x) for x in input().split()]
    dist = [int(x) for x in input().split()]

    dist.sort()
    min_dist = dist[0]
    for i in range(1, n):
        if dist[i] - dist[i - 1] < min_dist:
            min_dist = dist[i] - dist[i - 1]

    print(min_dist)

if __name__ == '__main__':
    main()
