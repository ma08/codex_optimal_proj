import sys
import math

def main():
    data = sys.stdin.readline().strip().split()
    counter = 0
    for i in range(len(data[0])):
        if i == len(data[0])-1:
            if data[0][i] != data[1][i]:
                counter += 1
            else:
                counter += 1
        elif i == len(data[0])-2:
            if data[0][i] == data[1][i] and data[0][i+1] == data[1][i+1]:
                counter += 1
            else:
                counter += 2
        else:
            if data[0][i] == data[1][i] and data[0][i+1] == data[1][i+1] and data[0][i+2] == data[1][i+2]:
                counter += 1
            else:
                counter += 2
    print(counter)

if __name__ == "__main__":
    main()
