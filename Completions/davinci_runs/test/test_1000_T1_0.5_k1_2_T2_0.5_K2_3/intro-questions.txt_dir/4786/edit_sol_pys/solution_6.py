

import sys

def main():
    n = int(sys.stdin.readline().strip())
    key_set = set()
    for i in range(n):
        key = sys.stdin.readline().strip().lower().replace("-", " ")
        key_set.add(key)
    print(len(key_set))

if __name__ == "__main__":
    main()

import os

def main(path):
    if os.path.exists(path):
        print(os.getcwd())
        return
    else:
        print(os.getcwd())
        os.mkdir(path)
        return

if __name__ == '__main__':
    main("/Users/wuxiaoxia/Desktop/Python/Python/test")
