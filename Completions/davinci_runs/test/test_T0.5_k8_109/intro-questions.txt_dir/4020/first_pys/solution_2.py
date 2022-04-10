

# Worked

def main():
    start = input()
    end = input()

    start = start.split(':')
    end = end.split(':')

    start = [int(x) for x in start]
    end = [int(x) for x in end]

    # print(start)
    # print(end)

    if start[1] == end[1]:
        print('{}:{}'.format(start[0], start[1]))
        return

    if start[1] == 0:
        start[1] = 60
        start[0] -= 1

    if end[1] == 0:
        end[1] = 60
        end[0] -= 1

    if start[0] == end[0]:
        if start[1] < end[1]:
            print('{}:{}'.format(start[0], int((start[1] + end[1]) / 2)))
        else:
            print('{}:{}'.format(start[0], int((start[1] + end[1] - 60) / 2)))
        return

    if start[0] < end[0]:
        print('{}:{}'.format(int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2)))
    else:
        print('{}:{}'.format(int((start[0] + end[0] - 24) / 2), int((start[1] + end[1]) / 2)))


if __name__ == "__main__":
    main()