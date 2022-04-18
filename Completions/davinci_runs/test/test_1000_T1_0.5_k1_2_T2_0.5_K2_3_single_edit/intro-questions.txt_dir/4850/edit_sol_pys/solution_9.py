

import math

def main():
    n = int(input()) # number of triangles
    triangles = [] # list of triangles
    for i in range(n): # iterate through each triangle
        triangles.append(tuple(map(int, input().split()))) # add the triangle to the list

    def get_area(triangle): # method to get area of triangle
        a, b, c = triangle
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_height(triangle): # method to get height of triangle
        a, b, c = triangle
        return (2 * get_area(triangle)) / c

    def get_angle(triangle): # method to get angle of triangle
        a, b, c = triangle
        return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        return math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    def get_rod_length(triangles): # method to get the length of the rod
        rod_length = 0
        for triangle in triangles:
            angle = get_angle(triangle) # get the angle of the triangle
            height = get_height(triangle) # get the height of the triangle
            rod_length += height * math.sin(angle) # add the length of the triangle to the rod length
        return rod_length

    print(get_rod_length(triangles)) # print the length of the rod


if __name__ == "__main__":
    main()
