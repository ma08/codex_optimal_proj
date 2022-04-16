
import math

def main():
    n = int(input())
    triangles = []
    for i in range(n):
        triangles.append(tuple(map(int, input().split())))

    def get_area(triangle):
        a, b, c = triangle
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_height(triangle):
        a, b, c = triangle
        return (2 * get_area(triangle)) / c

    def get_angle(triangle):
        a, b, c = triangle
        return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    def get_rod_length(triangles):
        rod_length = 0
        for triangle in triangles:
            angle = get_angle(triangle)
            height = get_height(triangle)
            rod_length += height * math.sin(angle)
        return rod_length

    print(get_rod_length(triangles))


if __name__ == "__main__":
    main()
