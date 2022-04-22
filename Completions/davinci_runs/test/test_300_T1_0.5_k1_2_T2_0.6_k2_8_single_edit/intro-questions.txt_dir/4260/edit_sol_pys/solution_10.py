import os

# from https://qiita.com/kazetof/items/1d902c7b2a2af0d7f8b8
def read_line():
    try:
        line = input()
        return line
    except:
        return None

def read_ints():
    return list(map(int, read_line().split(' ')))

def read_floats():
    return list(map(float, read_line().split(' ')))

def main():
    N, M = read_ints()
    print(N / M)

if __name__ == '__main__':
    main()
