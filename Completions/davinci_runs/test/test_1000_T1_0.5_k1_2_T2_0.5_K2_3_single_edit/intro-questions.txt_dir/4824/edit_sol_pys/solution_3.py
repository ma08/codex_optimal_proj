


def create_file(filename):
    with open(filename, "w") as file:
        file.write("")


def write_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()


def main():
    filename = "test.txt"
    create_file(filename)
    write_to_file(filename, "line 1")
    write_to_file(filename, "line 2")
    write_to_file(filename, "line 3")
    write_to_file(filename, "line 4")
    lines = read_file(filename)
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
