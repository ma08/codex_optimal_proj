import os

def create_file():
    with open("file.txt", "w") as file: # open file in write mode
        file.write("")

def write_file(text):
    with open("file.txt", "a") as file: # open file in append mode
        file.write(text + "\n")

def read_file():
    with open("file.txt", "r") as file: # open file in read mode
        print(file.read())

def delete_file():
    os.remove("file.txt") # delete file

def main():
    create_file()
    write_file("line 1")
    write_file("line 2")
    write_file("line 3")
    read_file()
    delete_file()

if __name__ == "__main__":
    main()
