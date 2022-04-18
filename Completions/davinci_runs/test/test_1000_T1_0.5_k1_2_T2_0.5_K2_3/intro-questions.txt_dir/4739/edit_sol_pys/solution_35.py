

def solve(N, M, T_array, X_array):
    #print("N: " + str(N))
    #print("M: " + str(M))
    #print("T_array: " + str(T_array))
    #print("X_array: " + str(X_array))
    speeds = set()
    for i in range(N-1):
        for j in range(i+1, N):
            speed = (X_array[j] - X_array[i]) / (T_array[j] - T_array[i])
            #print("speed: " + str(speed))
            speeds.add(speed)
    #print("speeds: " + str(speeds))
    distances = set()
    for speed in speeds:
        for i in range(N-1):
            for j in range(i+1, N):
                distance = (T_array[j] - T_array[i]) * speed + X_array[i]
                #print("distance: " + str(distance))
                distances.add(distance)
    #print("distances: " + str(distances))
    distances = list(distances)
    distances.sort()
    print(str(len(distances)))
    print(" ".join([str(x) for x in distances]))

if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]
    T_array = [int(x) for x in input().split()]
    X_array = [int(x) for x in input().split()]
    solve(M, N, T_array, X_array)
