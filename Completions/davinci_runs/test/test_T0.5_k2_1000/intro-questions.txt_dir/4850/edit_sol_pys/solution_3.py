import math


def main():
    n = int(input())
    triangles = []
    for _ in range(n):
        triangles.append(list(map(int, input().split())))

    def get_length(a, b, c):
        return (a + b + c) / 2

    def get_angle(a, b, c):
        return math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    def get_min_length(triangles):
        min_length = 0
        for triangle in triangles:
            a, b, c = triangle
            min_length = max(min_length, get_length(a, b, c) + get_length(a, c, b) * math.sin(get_angle(a, b, c)))
        return min_length

    print(get_min_length(triangles))


if __name__ == "__main__":
    main()
