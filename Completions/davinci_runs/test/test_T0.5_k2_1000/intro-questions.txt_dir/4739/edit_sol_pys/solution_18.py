

def solve(m, n, t_array, x_array):
    speeds = set()
    for i in range(m-1):
        for j in range(i+1, m):
            speed = (x_array[j] - x_array[i]) / (t_array[j] - t_array[i])
            speeds.add(speed)
    distances = set()
    for speed in speeds:
        for i in range(m-1):
            for j in range(i+1, m):
                distance = (t_array[j] - t_array[i]) * speed + x_array[i]
                distances.add(distance)
    distances = list(distances)
    distances.sort()
    print(len(distances))
    print(" ".join(str(x) for x in distances))

if __name__ == "__main__":
    m, n = [int(x) for x in input().split()]
    t_array = [int(x) for x in input().split()]
    x_array = [int(x) for x in input().split()]
    solve(m, n, t_array, x_array)
