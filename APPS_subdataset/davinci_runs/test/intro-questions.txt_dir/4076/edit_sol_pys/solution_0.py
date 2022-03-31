import math

# The distance between two points (x1, y1) and (x2, y2) is given by
# sqrt((x1 - x2)^2 + (y1 - y2)^2)
#
# The equation of a line passing through (x1, y1) and (x2, y2) is
# y - y1 = (y2 - y1) / (x2 - x1) * (x - x1)
#
# The equation of a line perpendicular to the line passing through (x1, y1) and (x2, y2) is
# y - y1 = -(x2 - x1) / (y2 - y1) * (x - x1)

# The distance between two points (x1, y1) and (x2, y2) is given by
# sqrt((x1 - x2)^2 + (y1 - y2)^2)
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# The equation of a line passing through (x1, y1) and (x2, y2) is
# y - y1 = (y2 - y1) / (x2 - x1) * (x - x1)
def getLine(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept

# The equation of a line perpendicular to the line passing through (x1, y1) and (x2, y2) is
# y - y1 = -(x2 - x1) / (y2 - y1) * (x - x1)
def getPerpendicularLine(x1, y1, x2, y2):
    slope = -(x2 - x1) / (y2 - y1)
    intercept = y1 - slope * x1
    return slope, intercept

# The intersection of two lines is given by the point
# x = (b1 - b2) / (m1 - m2)
# y = m1 * x + b1
def getIntersectionPoint(m1, b1, m2, b2):
    x = (b1 - b2) / (m1 - m2)
    y = m1 * x + b1
    return x, y

def getIntersectionPointFromLines(line1, line2):
    m1, b1 = line1
    m2, b2 = line2
    return getIntersectionPoint(m1, b1, m2, b2)

def getIntersectionPointFromLineAndPoint(line, point):
    m, b = line
    x, y = point
    return getIntersectionPoint(m, b, -1/m, y - 1/m * x)

def main():
    A, B, H, M = map(int, input().split())

    # Get the position of the hour and minute hands at time H:M
    thetaH = 2 * math.pi * (H + M / 60) / 12
    thetaM = 2 * math.pi * M / 60
    xH, yH = A * math.sin(thetaH), A * math.cos(thetaH)
    xM, yM = B * math.sin(thetaM), B * math.cos(thetaM)

    # Get the lines that the hour and minute hands make
    lineH = getLine(0, 0, xH, yH)
    lineM = getLine(0, 0, xM, yM)

    # Get the line perpendicular to the minute hand that passes through the hour hand.
    linePerpM = getPerpendicularLine(xM, yM, xH, yH)

    # Get the intersection point of the line perpendicular to the minute hand and the minute hand.
    xI, yI = getIntersectionPointFromLines(lineM, linePerpM)

    # Get the distance between the intersection point and the hour hand.
    print(getDistance(xH, yH, xI, yI))

if __name__ == '__main__':
    main()
