import os
import sys

def create_file(filename):
    with open(filename, 'w') as f:
        f.write("")

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def delete_file(filename):
    os.remove(filename)

def delete_folder(directory):
    os.rmdir(directory)

def move_file(filename, destination):
    os.rename(filename, destination)

def copy_file(filename, destination):
    with open(filename, 'r') as f:
        with open(destination, 'w') as f1:
            for line in f:
                f1.write(line)

def main():
    create_file("test.txt")
    create_folder("test")
    move_file("test.txt", "test/test.txt")
    copy_file("test/test.txt", "test/test1.txt")
    delete_file("test/test.txt")
    delete_folder("test")

if __name__ == "__main__":
    main()
