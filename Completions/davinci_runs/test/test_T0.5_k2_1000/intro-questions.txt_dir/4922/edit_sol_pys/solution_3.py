
import os
def main():
    print("Current working directory is: " + os.getcwd()) # current working directory
    os.chdir("C:\\Users\\Vikas\\Desktop\\Python") # change directory
    print("Current working directory is: " + os.getcwd()) # current working directory
    print("List of files in directory: " + os.getcwd()) # list of files in directory
    print(os.listdir("C:\\Users\\Vikas\\Desktop\\Python")) # list of files in directory

if __name__ == '__main__':
    main()
