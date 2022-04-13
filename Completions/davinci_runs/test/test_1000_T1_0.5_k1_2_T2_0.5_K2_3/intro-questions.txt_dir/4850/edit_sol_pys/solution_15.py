
def main():
    n = int(input())
    triangles = []
    for _ in range(n):
        triangles.append(list(map(int, input().split())))

    def get_length(a, b):
        return ((a**2 + b**2)**0.5) / 2

    def get_angle(a, b):
        return math.acos(0.5 * a / b)

    def get_max_length(triangles):
        max_length = 0
        for triangle in triangles:
            a, b, c = triangle
            max_length = max(max_length, get_length(a, b) + get_length(c, b) * math.sin(get_angle(a, b)))
        return max_length

    print(get_max_length(triangles))


if __name__ == "__main__":
    main()
