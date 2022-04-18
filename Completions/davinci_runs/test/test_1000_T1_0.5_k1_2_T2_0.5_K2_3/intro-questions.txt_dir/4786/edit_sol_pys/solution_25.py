

# import sys

# def main():
#     n = int(sys.stdin.readline().strip())
#     key_set = set()
#     for i in range(n):
#         key = sys.stdin.readline().strip().lower().replace("-", " ")
#         key_set.add(key)
#     print(len(key_set))

# if __name__ == "__main__":
#     main()

import os

def main(path):
    if not os.path.exists(path):
        os.makedirs(path)
    print(os.getcwd())

if __name__ == '__main__':
    main("/Users/wuxiaoxia/Desktop/Python/Python/test/test1/test2")
