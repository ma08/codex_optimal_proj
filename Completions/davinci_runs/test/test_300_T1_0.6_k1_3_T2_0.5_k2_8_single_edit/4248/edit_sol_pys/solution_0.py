
def main():
    number_of_points = int(input())
    point_list = []
    for _ in range(number_of_points):
        point_list.append(list(map(float, input().split())))
    max_length = 0
    for i in range(number_of_points - 1):
        for j in range(i + 1, number_of_points):
            length = ((point_list[i][0] - point_list[j][0])**2 + (point_list[i][1] - point_list[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    print(max_length)


if __name__ == "__main__":
    main()
