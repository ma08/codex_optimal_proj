

def get_min_diff(string):
    min_diff = 1000
    for i in range(len(string) - 2):
        difference = abs(753 - int(string[i:i+3]))
        if difference < min_diff:
            min_diff = difference
    return min_diff

if __name__ == '__main__':
    string = input()
    print(get_min_diff(string))
