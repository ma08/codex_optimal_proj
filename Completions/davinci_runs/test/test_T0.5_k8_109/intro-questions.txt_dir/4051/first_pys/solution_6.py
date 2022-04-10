

import sys

def main():
    lines = sys.stdin
    next(lines)
    data = [int(x) for x in next(lines).split()]
    if can_sort(data):
        print("YES")
    else:
        print("NO")

def can_sort(data):
    if len(data) <= 2:
        return True
    else:
        max_index = index_max(data)
        current_max = data[max_index]
        data = data[:max_index] + data[max_index+1:]
        if len(data) > 2:
            if data[-1] == current_max - 1:
                if data[-2] == current_max - 2:
                    return can_sort(data[:-2] + [current_max - 1])
                else:
                    return can_sort(data[:-1] + [current_max - 1])
            else:
                return can_sort(data)
        else:
            return data[0] == current_max - 1

def index_max(data):
    max_index = 0
    for i in range(len(data)):
        if data[i] > data[max_index]:
            max_index = i
    return max_index

if __name__ == '__main__':
    main()