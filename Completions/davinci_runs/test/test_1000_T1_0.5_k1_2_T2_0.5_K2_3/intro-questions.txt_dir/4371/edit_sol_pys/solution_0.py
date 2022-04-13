
def get_min_dif(string):
    min_dif = 1001
    for i in range(len(string) - 2):
        dif = abs(753 - int(string[i:i+3]))
        if dif < min_dif:
            min_dif = dif
    return min_dif

if __name__ == '__main__':
    string = input()
    print(get_min_dif(string))
