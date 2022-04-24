def write():
    with open("example.txt", "w") as file:
        file.write("Line one\n")
        file.write("Line two\n")
        file.write("Line three\n")

def read_all():
    with open("example.txt", "r") as file:
        print(file.read())

def read_line():
    with open("example.txt", "r") as file:
        print(file.readline())

def read_lines():
    with open("example.txt", "r") as file:
        for line in file:
            print(line)

def append():
    with open("example.txt", "a") as file:
        file.write("Line four\n")

def main():
    write()
    read_all()
    read_line()
    read_lines()
    append()

if __name__ == "__main__":
    main()
