
def read_line():
    return input()

def read_ints():
    return list(map(int, read_line().split(' ')))

def read_floats():
    return list(map(float, read_line().split(' ')))

def main():
    A, B = read_ints()
    print(A + B)

if __name__ == '__main__':
    main()
