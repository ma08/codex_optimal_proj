

def solve(M, N, T_array, X_array):
    #print("M: " + str(M))
    #print("N: " + str(N))
    #print("T_array: " + str(T_array))
    #print("X_array: " + str(X_array))
    speeds = set()
    for i in range(M-1):
        for j in range(i+1, M):
            speed = (X_array[j] - X_array[i]) / (T_array[j] - T_array[i])
            #print("speed: " + str(speed))
            speeds.add(speed)
    #print("speeds: " + str(speeds))
    distances = set()
    for speed in speeds:
        for i in range(M-1):
            for j in range(i+1, M):
                distance = (T_array[j] - T_array[i]) * speed + X_array[i]
                #print("distance: " + str(distance))
                distances.add(distance)
    #print("distances: " + str(distances))
    distances = list(distances)
    distances.sort()
    print(len(distances))
    print(" ".join(str(x) for x in distances)) 

if __name__ == "__main__":
    M, N = [int(x) for x in input().split()]
    T_array = [int(x) for x in input().split()]
    X_array = [int(x) for x in input().split()]
    solve(M, N, T_array, X_array)
