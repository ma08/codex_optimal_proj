
def read_file(filename):
    with open(filename) as f:
        for line in f:
            print(line)
read_file("file.txt")
