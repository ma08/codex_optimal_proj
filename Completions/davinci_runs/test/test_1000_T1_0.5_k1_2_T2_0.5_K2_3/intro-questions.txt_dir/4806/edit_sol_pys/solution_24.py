
import sys
import math

def main():
    data = sys.stdin.readline().strip()
    counter = 0
    for i in range(len(data)):
        if i == len(data)-1:
            counter += 1
        elif i == len(data)-2 and data[i] == data[i+1]:
            counter += 1
        elif i == len(data)-2 and data[i] != data[i+1]:
            counter += 2
        elif i == len(data)-3 and data[i] == data[i+1] and data[i+1] == data[i+2]:
            counter += 1
        elif i == len(data)-3 and data[i] == data[i+1] and data[i+1] != data[i+2]:
            counter += 2
        elif i == len(data)-3 and data[i] != data[i+1] and data[i+1] == data[i+2]:
            counter += 2
        elif i == len(data)-3 and data[i] != data[i+1] and data[i+1] != data[i+2]:
            counter += 3
        elif i == len(data)-4 and data[i] == data[i+1] and data[i+1] == data[i+2] and data[i+2] == data[i+3]:
            counter += 1
        elif i == len(data)-4 and data[i] == data[i+1] and data[i+1] == data[i+2] and data[i+2] != data[i+3]:
            counter += 2
        elif i == len(data)-4 and data[i] == data[i+1] and data[i+1] != data[i+2] and data[i+2] == data[i+3]:
            counter += 2
        elif i == len(data)-4 and data[i] == data[i+1] and data[i+1] != data[i+2] and data[i+2] != data[i+3]:
            counter += 3
        elif i == len(data)-4 and data[i] != data[i+1] and data[i+1] == data[i+2] and data[i+2] == data[i+3]:
            counter += 2
        elif i == len(data)-4 and data[i] != data[i+1] and data[i+1] == data[i+2] and data[i+2] != data[i+3]:
            counter += 3
        elif i == len(data)-4 and data[i] != data[i+1] and data[i+1] != data[i+2] and data[i+2] == data[i+3]:
            counter += 3
        elif i == len(data)-4 and data[i] != data[i+1] and data[i+1] != data[i+2] and data[i+2] != data[i+3]:
            counter += 4
        elif data[i] == data[i+1] and data[i+1] == data[i+2]:
            counter += 1
        elif data[i] == data[i+1] and data[i+1] != data[i+2]:
            counter += 2
        elif data[i] != data[i+1] and data[i+1] == data[i+2]:
            counter += 2
        elif data[i] != data[i+1] and data[i+1] != data[i+2]:
            counter += 3
        else:
            counter += 2
        '''
        if data[i] == data[i+1] and data[i+1] == data[i+2]:
            counter += 1
        elif data[i] == data[i+1] and data[i+1] != data[i+2]:
            counter += 2
        elif data[i] != data[i+1] and data[i+1] == data[i+2]:
            counter += 2
        elif data[i] != data[i+1] and data[i+1] != data[i+2]:
            if data[i] == data[i+1]:
                counter += 1
            else:
                counter += 2
        else:
            if data[i] == data[i+1] and data[i+1] == data[i+2]:
                counter += 1
            else:
                counter += 2
        '''
    print(counter)

if __name__ == "__main__":
    main()
