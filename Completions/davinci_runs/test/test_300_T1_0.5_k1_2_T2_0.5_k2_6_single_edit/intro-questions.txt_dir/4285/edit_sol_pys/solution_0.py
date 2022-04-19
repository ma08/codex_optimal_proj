

import sys

def main():
    # read number of lines
    n = int(input())

    # read lines
    lines = [input() for _ in range(n)]

    # count number of lines that contain g
    count = 0
    for line in lines:
        if 'g' in line:
            count += 1

    # print the number of lines that contain g
    print(str(count))

if __name__ == '__main__':
    main()
