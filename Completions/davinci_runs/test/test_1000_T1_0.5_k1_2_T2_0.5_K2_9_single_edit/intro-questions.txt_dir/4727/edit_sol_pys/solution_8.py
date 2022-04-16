

import copy

def array_transpose(arr):
    return [[arr[j][i] for j in range(len(arr))]
            for i in range(len(arr[0]))]

def move_left(data):
    """
    1. Remove all zeros
    2. Merge all pairs
    3. Remove all zeros
    4. Fill remaining with zeros
    """
    for i in range(len(data)):
        data[i] = [x for x in data[i] if x]
        for j in range(len(data[i])-1):
            if data[i][j] == data[i][j+1]:
                data[i][j] = data[i][j] * 2
                data[i][j+1] = 0
        data[i] = [x for x in data[i] if x]
        data[i] += [0] * (4 - len(data[i]))
    return data

def move_right(data):
    """
    1. Reverse all rows
    2. Remove all zeros
    3. Merge all pairs
    4. Remove all zeros
    5. Fill remaining with zeros
    6. Reverse all rows
    """
    for i in range(len(data)):
        data[i] = data[i][::-1]
        data[i] = [x for x in data[i] if x]
        for j in range(len(data[i])-1):
            if data[i][j] == data[i][j+1]:
                data[i][j] = data[i][j] * 2
                data[i][j+1] = 0
        data[i] = [x for x in data[i] if x]
        data[i] += [0] * (4 - len(data[i]))
        data[i] = data[i][::-1]
    return data

def move_up(data):
    """
    1. Transpose
    2. Remove all zeros
    3. Merge all pairs
    4. Remove all zeros
    5. Fill remaining with zeros
    6. Transpose
    """
    data = array_transpose(data)
    for i in range(len(data)):
        data[i] = [x for x in data[i] if x]
        for j in range(len(data[i])-1):
            if data[i][j] == data[i][j+1]:
                data[i][j] = data[i][j] * 2
                data[i][j+1] = 0
        data[i] = [x for x in data[i] if x]
        data[i] += [0] * (4 - len(data[i]))
    data = array_transpose(data)
    return data

def move_down(data):
    """
    1. Transpose
    2. Reverse all rows
    3. Remove all zeros
    4. Merge all pairs
    5. Remove all zeros
    6. Fill remaining with zeros
    7. Reverse all rows
    8. Transpose
    """
    data = array_transpose(data)
    for i in range(len(data)):
        data[i] = data[i][::-1]
        data[i] = [x for x in data[i] if x]
        for j in range(len(data[i])-1):
            if data[i][j] == data[i][j+1]:
                data[i][j] = data[i][j] * 2
                data[i][j+1] = 0
        data[i] = [x for x in data[i] if x]
        data[i] += [0] * (4 - len(data[i]))
        data[i] = data[i][::-1]
    data = array_transpose(data)
    return data

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
