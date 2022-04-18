

def is_inside(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 >= x3 and x1 <= x4 and y1 >= y3 and y1 <= y4)

def is_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 >= x3 and x1 <= x4 and y1 >= y3 and y1 <= y4) or (x2 >= x3 and x2 <= x4 and y2 >= y3 and y2 <= y4) or (x1 >= x5 and x1 <= x6 and y1 >= y5 and y1 <= y6) or (x2 >= x5 and x2 <= x6 and y2 >= y5 and y2 <= y6)

def is_outside(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1 < x3 and x2 > x4 and y1 < y3 and y2 > y4)

def is_inside_and_outside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (not is_inside(x1, y1, x3, y3, x4, y4, x5, y5)) and (not is_inside(x2, y2, x3, y3, x4, y4, x5, y5)) and (not is_inside(x1, y1, x3, y3, x4, y4, x6, y6)) and (not is_inside(x2, y2, x3, y3, x4, y4, x6, y6))

def is_outside_and_outside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_outside(x1, y1, x2, y2, x3, y3, x4, y4)) and (is_outside(x1, y1, x2, y2, x5, y5, x6, y6))

def is_overlap_and_outside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_overlap(x1, y1, x2, y2, x3, y3, x4, y4)) and (is_outside(x1, y1, x2, y2, x5, y5, x6, y6))

def is_overlap_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_overlap(x1, y1, x2, y2, x3, y3, x4, y4)) and (is_overlap(x1, y1, x2, y2, x5, y5, x6, y6))

def is_outside_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_outside(x1, y1, x2, y2, x3, y3, x4, y4)) and (is_overlap(x1, y1, x2, y2, x5, y5, x6, y6))

def is_outside_and_inside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_outside(x1, y1, x2, y2, x3, y3, x4, y4)) and (not is_outside(x1, y1, x2, y2, x5, y5, x6, y6))

def is_overlap_and_inside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (is_overlap(x1, y1, x2, y2, x3, y3, x4, y4)) and (not is_outside(x1, y1, x2, y2, x5, y5, x6, y6))

def is_inside_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (not is_outside(x1, y1, x2, y2, x3, y3, x4, y4)) and (is_overlap(x1, y1, x2, y2, x5, y5, x6, y6))

def is_inside_and_inside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return (not is_outside(x1, y1, x2, y2, x3, y3, x4, y4)) and (not is_outside(x1, y1, x2, y2, x5, y5, x6, y6))


if __name__ == "__main__":
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x3, y3, x4, y4 = tuple(map(int, input().split()))
    x5, y5, x6, y6 = tuple(map(int, input().split()))

    if (is_outside_and_outside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_overlap_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_outside_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_outside_and_inside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_overlap_and_inside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_inside_and_overlap(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) or
    is_inside_and_outside(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)):
        print('YES')
    else:
        print('NO')
