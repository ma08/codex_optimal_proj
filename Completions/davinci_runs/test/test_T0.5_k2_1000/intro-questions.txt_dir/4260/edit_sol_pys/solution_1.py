

# from https://qiita.com/kazetof/items/1d902c7b2a2af0d7f8b8
def read_line():
    try:
        line = input()
        return line
    except EOFError:
        return None

def read_ints():
    return list(map(int, read_line().split(' ')))

def read_floats():
    return list(map(float, read_line().split(' ')))

def main():
    a, b = read_ints()
    print(a + b)

if __name__ == '__main__':
    main()
