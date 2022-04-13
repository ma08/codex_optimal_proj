

def main():
    data = []
    for _ in range(4):
        data.append([int(x) for x in input().split()])
    direction = int(input())
    if direction == 0:
        data = move_left(copy.deepcopy(data))
    elif direction == 1:
        data = move_up(copy.deepcopy(data))
    elif direction == 2:
        data = move_right(copy.deepcopy(data))
    elif direction == 3:
        data = move_down(copy.deepcopy(data))
    for row in data:
        print(*row)

if __name__ == '__main__':
    main()
