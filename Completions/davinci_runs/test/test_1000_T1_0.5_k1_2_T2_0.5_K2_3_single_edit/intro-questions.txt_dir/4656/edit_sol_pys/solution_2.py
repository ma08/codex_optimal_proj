import os
import shutil


    os.chdir(r"C:\Users\Student\Desktop")
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            shutil.copy(filename, filename + '.bak')
def main():
    pass


if __name__ == "__main__":
    main()
