import os
import sys
import time


def main():
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path does not exist")
        return
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            filename = os.path.join(root, file)
            print(filename)
            print(os.path.getctime(filename))
            print(time.ctime(os.path.getctime(filename)))


if __name__ == '__main__':
    main()
