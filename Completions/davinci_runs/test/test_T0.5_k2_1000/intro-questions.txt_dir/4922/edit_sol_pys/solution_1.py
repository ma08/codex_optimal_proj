
import os
def main():
    print("Current working directory is: " + str(os.getcwd()))
    os.chdir("C:\\Users\\Vikas\\Desktop\\Python")
    print("Current working directory is: " + str(os.getcwd()))
    print("List of files in directory: " + str(os.getcwd()))
    print(os.listdir("C:\\Users\\Vikas\\Desktop\\Python"))

if __name__ == '__main__':
    main()
