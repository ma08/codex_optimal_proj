

from math import sqrt


def main():
    # Read the input data.
    """
    The main function
    """
    num_corners = int(input().strip())
    corners = []
    # Calculate the area of the polygon.
    polygon_area = 0
    for i in range(num_corners):
        x1, y1 = corners[i]
        x2, y2 = corners[(i + 1) % num_corners]
        polygon_area += x1 * y2 - x2 * y1
    polygon_area = abs(polygon_area / 2)
    # Calculate the distance between the center of mass and the center of
    # the polygon.
    center_x = sum([x for x, y in corners]) / num_corners
    center_y = sum([y for x, y in corners]) / num_corners
    center_mass_x = sum([x * (x1 * y2 - x2 * y1) for i in range(num_corners)]) / 6 / polygon_area
    center_mass_y = sum([y * (x1 * y2 - x2 * y1) for i in range(num_corners)]) / 6 / polygon_area
    distance = sqrt((center_mass_x - center_x) ** 2 + (center_mass_y - center_y) ** 2)
    # Calculate the area of the circle.
    circle_area = distance ** 2 * 3.14159265358979
    # Calculate the area of the polygon.
    for _ in range(num_corners):
        x, y = input().strip().split()
        corners.append((float(x), float(y)))
    area = int(input().strip())
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
