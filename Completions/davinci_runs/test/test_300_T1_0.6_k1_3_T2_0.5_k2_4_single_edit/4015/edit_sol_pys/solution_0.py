import os
import time
import sys

# file
def file():
    try:
        file = open("file.txt", "x")
        file.write("This is a test file")
    except FileExistsError:
        print("File already exists")

# print file
def print_file():
    try:
        file = open("file.txt", "r")
        print(file.read())
    except FileNotFoundError:
        print("File doesn't exist")

# delete file
def delete_file():
    try:
        os.remove("file.txt")
        print("File has been deleted")
    except FileNotFoundError:
        print("File doesn't exist")

# create directory
def directory():
    try:
        os.mkdir("test")
    except FileExistsError:
        print("Directory already exists")

# delete directory
def delete_directory():
    try:
        os.rmdir("test")
    except FileNotFoundError:
        print("Directory doesn't exist")

# rename directory
def rename_directory():
    try:
        os.rename("test", "test2")
    except FileNotFoundError:
        print("Directory doesn't exist")

# rename file
def rename_file():
    try:
        os.rename("file.txt", "test.txt")
    except FileNotFoundError:
        print("File doesn't exist")

# print working directory
def print_wd():
    print(os.getcwd())

# change working directory
def change_wd():
    try:
        os.chdir("/Users/mohammed/Desktop")
        print(os.getcwd())
    except FileNotFoundError:
        print("Directory doesn't exist")

# list directory
def list_directory():
    print(os.listdir())

# print system information
def system_info():
    print(sys.version)

# print current date and time
def date_time():
    print(time.localtime())

# exception handling
def exception():
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("You can't divide by zero")

# print menu
def menu():
    options = {
        "a": file,
        "b": print_file,
        "c": delete_file,
        "d": directory,
        "e": delete_directory,
        "f": rename_directory,
        "g": rename_file,
        "h": print_wd,
        "i": change_wd,
        "j": list_directory,
        "k": system_info,
        "l": date_time,
        "m": exception
    }

    print("(a) Create file")
    print("(b) Print file")
    print("(c) Delete file")
    print("(d) Create directory")
    print("(e) Delete directory")
    print("(f) Rename directory")
    print("(g) Rename file")
    print("(h) Print working directory")
    print("(i) Change working directory")
    print("(j) List directory")
    print("(k) System information")
    print("(l) Current date and time")
    print("(m) Exception handling")

    choice = input("Choose an option: ")

    if choice in options:
        options[choice]()
    else:
        print("Invalid option")

    menu()

menu()
