import sys
import math

def main():
    data = sys.stdin.readline().strip()
    counter = 1
    for i in range(len(data)):
        if data[i] == data[i+1]:
            counter += 1
        else:
            counter += 1
    print(counter)

if __name__ == "__main__":
    main()
