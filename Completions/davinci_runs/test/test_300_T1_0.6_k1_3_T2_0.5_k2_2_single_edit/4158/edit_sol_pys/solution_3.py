

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Calculate the maximum number of points that satisfy the given condition
    max_points = []
    for point_idx in range(n):
        point = a[point_idx]
        temp_max_points = [point]
        for pow_idx in range(1, 30):
            # We check that there are points at a distance of 2^1, 2^2, 2^3, ..., 2^29
            if (point + 2**pow_idx in a) and (point - 2**pow_idx in a):
                temp_max_points.append(point + 2**pow_idx)
                temp_max_points.append(point - 2**pow_idx)
            else:
                break
        if len(temp_max_points) > len(max_points):
            max_points = temp_max_points

    max_points.sort()

    print(len(max_points))
    print(*max_points)

if __name__ == "__main__":
    main()
