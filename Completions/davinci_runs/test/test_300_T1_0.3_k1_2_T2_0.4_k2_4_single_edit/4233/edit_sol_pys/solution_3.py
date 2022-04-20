

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(line)

if __name__ == "__main__":
    read_file("file.txt")
