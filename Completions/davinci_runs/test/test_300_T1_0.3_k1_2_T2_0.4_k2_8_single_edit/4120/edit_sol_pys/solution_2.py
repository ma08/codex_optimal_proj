
import math
import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]

    #print(n, m, k)
    #print(roads)

    # get the distance between each city
    distances = [[0 for x in range(n)] for y in range(n)]
    for road in roads:
        distances[road[0]][road[1]] = road[2]
        distances[road[1]][road[0]] = road[2]

    #print(distances)

    # get the distance between each city and the warehouse
    warehouse = []
    for i in range(k):
        warehouse.append(int(sys.stdin.readline()))

    #print(warehouse)

    # get the distance between each city and the warehouse
    for i in range(n):
        for j in range(k):
            distances[i][warehouse[j]] = math.sqrt(distances[i][warehouse[j]] ** 2 + 1 ** 2)
            distances[warehouse[j]][i] = distances[i][warehouse[j]]

    #print(distances)

    # get the shortest distance between each city
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][0] + distances[0][j]:
                distances[i][j] = distances[i][0] + distances[0][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][1] + distances[1][j]:
                distances[i][j] = distances[i][1] + distances[1][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][2] + distances[2][j]:
                distances[i][j] = distances[i][2] + distances[2][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][3] + distances[3][j]:
                distances[i][j] = distances[i][3] + distances[3][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][4] + distances[4][j]:
                distances[i][j] = distances[i][4] + distances[4][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][5] + distances[5][j]:
                distances[i][j] = distances[i][5] + distances[5][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][6] + distances[6][j]:
                distances[i][j] = distances[i][6] + distances[6][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][7] + distances[7][j]:
                distances[i][j] = distances[i][7] + distances[7][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][8] + distances[8][j]:
                distances[i][j] = distances[i][8] + distances[8][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][9] + distances[9][j]:
                distances[i][j] = distances[i][9] + distances[9][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][10] + distances[10][j]:
                distances[i][j] = distances[i][10] + distances[10][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][11] + distances[11][j]:
                distances[i][j] = distances[i][11] + distances[11][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][12] + distances[12][j]:
                distances[i][j] = distances[i][12] + distances[12][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][13] + distances[13][j]:
                distances[i][j] = distances[i][13] + distances[13][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][14] + distances[14][j]:
                distances[i][j] = distances[i][14] + distances[14][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][15] + distances[15][j]:
                distances[i][j] = distances[i][15] + distances[15][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][16] + distances[16][j]:
                distances[i][j] = distances[i][16] + distances[16][j]

    #print(distances)

    # get the shortest distance between each city
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][17] + distances[17][j]:
                distances[i][j] = distances[i][17

if __name__ == "__main__":
    main()
