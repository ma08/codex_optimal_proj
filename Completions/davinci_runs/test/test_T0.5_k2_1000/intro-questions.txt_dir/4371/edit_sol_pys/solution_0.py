

def get_min_diff(string):
    min_diff = 1001
    for i in range(len(string) - 2):  # 最後の二桁は753にならないので
        diff = abs(753 - int(string[i:i + 3]))
        if diff < min_diff:
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    string = input()
    print(get_min_diff(string))
