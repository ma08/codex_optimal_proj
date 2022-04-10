
#-----------------------------------------------------------------------------#

def is_inside(x1, x2, x3, x4):
    if x3 < x1 and x4 > x2:
        return True
    return False

def is_outside(x1, x2, x3, x4):
    if x3 > x1 and x4 < x2:
        return True
    return False

def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    if is_inside(x1, x2, x3, x4) and is_inside(x1, x2, x5, x6):
        return False
    if is_outside(x1, x2, x3, x4) and is_outside(x1, x2, x5, x6):
        return False
    return True

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

if is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    print('YES')
else:
    print('NO')
