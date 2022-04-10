import os

def create_file():
    with open("file.txt", "w") as file_:
        file.write("")

def write_file(text):
    with open("file.txt", "a") as file_:
        file_.write(text + "\n")

def read_file():
    with open("file.txt", "r") as file_:
        print(file_.read())

def delete_file():
    os.remove("file.txt")

def main():
    create_file()
    write_file("line 1")
    write_file("line 2")
    write_file("line 3")
    read_file()
    delete_file()

if __name__ == "__main__":
    main()
