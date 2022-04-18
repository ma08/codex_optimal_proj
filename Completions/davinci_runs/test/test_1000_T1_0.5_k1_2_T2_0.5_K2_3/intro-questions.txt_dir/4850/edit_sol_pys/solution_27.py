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

    def get_sin_angle(triangle):
        a, b, c = triangle
        return math.sin(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))

    def get_rope_length(triangles):
        rope_length = 0
        for triangle in triangles:
            sin_angle = get_sin_angle(triangle)
            height = get_height(triangle)
            rope_length += height * sin_angle
        return round(rope_length, 2)

    print(get_rod_length(triangles))


if __name__ == "__main__":
    main()
