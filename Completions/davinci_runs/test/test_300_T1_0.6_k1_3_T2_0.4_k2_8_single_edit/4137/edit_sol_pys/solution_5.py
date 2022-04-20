


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

if __name__ == "__main__":
    print(read_file('test.txt'))
