

def solve(M, N, T_list, X_list):
    # print("M: " + str(M))
    # print("N: " + str(N))
    # print("T_list: " + str(T_list))
    # print("X_list: " + str(X_list))
    speeds = set()
    for i in range(M - 1):
        for j in range(i + 1, M):
            speed = (X_list[j] - X_list[i]) / (T_list[j] - T_list[i])
            # print("speed: " + str(speed))
            speeds.add(speed)
    # print("speeds: " + str(speeds))
    distances = set()
    for speed in speeds:
        for i in range(M - 1):
            for j in range(i + 1, M):
                distance = (T_list[j] - T_list[i]) * speed + X_list[i]
                # print("distance: " + str(distance))
                distances.add(distance)
    # print("distances: " + str(distances))
    distances = list(distances)
    distances.sort()
    print(len(distances))
    print(" ".join(str(x) for x in distances))


if __name__ == "__main__":
    M, N = [int(x) for x in input().split()]
    T_list = [int(x) for x in input().split()]
    X_list = [int(x) for x in input().split()]
    solve(M, N, T_list, X_list)
