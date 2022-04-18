
import sys

def main():
    my_file = open("file.txt", "r")
    print(my_file.readline())
    my_file.close()

main()
