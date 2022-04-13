

import sys,os

def main():
    print(os.path.abspath("file.py"))
    print(os.path.exists("file.py"))
    print(os.path.isdir("file.py"))
    print(os.path.isfile("file.py"))
    print(os.path.getsize("file.py"))
    print(os.path.split("/home/peng/file.py"))
    print(os.path.splitext("/home/peng/file.py"))
    print(os.path.join("/home/peng","file.py"))

if __name__ == "__main__":
    main()
