

# from https://qiita.com/kazetof/items/1d902c7b2a2af0d7f8b8 (edited)

def read_line():
    try:
        line = input()
        return line
    except:
        return None

def read_int():
    return int(read_line())

def read_ints(n=None):
    if n:
        return list(map(int, read_line().split(' ')))[:n]
    else:
        return list(map(int, read_line().split(' ')))

def read_float():
    return float(read_line())

def read_floats(n=None):
    if n:
        return list(map(float, read_line().split(' ')))[:n]
    else:
        return list(map(float, read_line().split(' ')))


def main():

    T = read_int()
    for i in range(T):
        N = read_int()
        print(N)


if __name__ == '__main__':
    main()
