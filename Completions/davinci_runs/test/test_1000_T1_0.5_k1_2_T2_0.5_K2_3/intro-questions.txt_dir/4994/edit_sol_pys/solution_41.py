

# Read input 
points = []
for _ in range(3):
    points.append([int(x) for x in input().split()])

# Get the fourth point
for i in range(3):
    for j in range(i+1, 3):
        if points[i][0] == points[j][0] and points[i][1] != points[j][1]:
            # Two points have the same x coordinate, but different y coordinates
            # The fourth point must have the same x coordinate as the other two, but the same y coordinate as the third point
            print(points[i][0], points[3-i-j][1])
            break
        elif points[i][1] == points[j][1] and points[i][0] != points[j][0]:
            # Two points have the same y coordinate, but different x coordinates
            # The fourth point must have the same y coordinate as the other two, but the same x coordinate as the third point
            print(points[3-i-j][0], points[i][1])
            break
        elif i == 2 and j == 3:
            # If we haven't found the fourth point, that means the points are not collinear
            # The fourth point must have the same x coordinate as one point, and the same y coordinate as the other point
            print(points[0][0], points[2][1])
