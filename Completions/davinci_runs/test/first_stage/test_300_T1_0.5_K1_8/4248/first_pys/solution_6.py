
import math

def check_angle(x1, y1, x2, y2):
    if x2 == x1:
        if y2 > y1:
            return 90
        else:
            return 270
    else:
        return math.degrees(math.atan((y2-y1)/(x2-x1)))

def get_angle(x1, y1, x2, y2):
    if x2 < x1:
        return check_angle(x2, y2, x1, y1)+180
    elif y2 < y1:
        return check_angle(x2, y2, x1, y1)+360
    else:
        return check_angle(x2, y2, x1, y1)

def get_min_angle(x1, y1, x2, y2, x3, y3):
    angle1 = get_angle(x1, y1, x2, y2)
    angle2 = get_angle(x1, y1, x3, y3)
    angle3 = get_angle(x2, y2, x3, y3)
    min_angle = min(angle1, angle2, angle3)
    if min_angle == angle1:
        return x2, y2
    elif min_angle == angle2:
        return x3, y3
    else:
        return x1, y1

def get_min_dist(x1, y1, x2, y2, x3, y3):
    x, y = get_min_angle(x1, y1, x2, y2, x3, y3)
    return math.sqrt((x1-x)**2 + (y1-y)**2)

def get_max_dist(x1, y1, x2, y2, x3, y3):
    x, y = get_min_angle(x1, y1, x2, y2, x3, y3)
    return math.sqrt((x2-x)**2 + (y2-y)**2)

def get_angle_diff(x1, y1, x2, y2, x3, y3):
    angle1 = get_angle(x1, y1, x2, y2)
    angle2 = get_angle(x1, y1, x3, y3)
    angle3 = get_angle(x2, y2, x3, y3)
    return min(abs(angle1-angle2), abs(angle1-angle3), abs(angle2-angle3))

def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

def get_perimeter(x1, y1, x2, y2, x3, y3):
    return get_min_dist(x1, y1, x2, y2, x3, y3) + get_max_dist(x1, y1, x2, y2, x3, y3) + math.sqrt((x3-x2)**2 + (y3-y2)**2)

n = int(input())
x = []
y = []
for i in range(n):
    a, b = input().split(" ")
    x.append(float(a))
    y.append(float(b))

min_area = 10000000000
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            area = get_area(x[i], y[i], x[j], y[j], x[k], y[k])
            if area < min_area:
                min_area = area
                min_perimeter = get_perimeter(x[i], y[i], x[j], y[j], x[k], y[k])
                min_angle_diff = get_angle_diff(x[i], y[i], x[j], y[j], x[k], y[k])
            elif area == min_area:
                perimeter = get_perimeter(x[i], y[i], x[j], y[j], x[k], y[k])
                angle_diff = get_angle_diff(x[i], y[i], x[j], y[j], x[k], y[k])
                if perimeter < min_perimeter:
                    min_perimeter = perimeter
                    min_angle_diff = angle_diff
                elif perimeter == min_perimeter:
                    if angle_diff < min_angle_diff:
                        min_angle_diff = angle_diff

print(min_perimeter)