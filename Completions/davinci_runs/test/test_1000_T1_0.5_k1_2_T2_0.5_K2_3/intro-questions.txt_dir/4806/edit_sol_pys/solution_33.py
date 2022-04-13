
import sys
import math

def main():
    data = sys.stdin.readline().strip()
    counter = 0
    for i in range(len(data)):
        if i == len(data)-1:
            counter += 1
        elif i == len(data)-2:
            if data[i] == data[i+1]:
                counter += 1
            else:
                counter += 2
        else:
            if data[i] == data[i+1] or data[i+1] == data[i+2]:
                counter += 1
            else:
                counter += 2
    print(counter)

if __name__ == "__main__":
    main()
