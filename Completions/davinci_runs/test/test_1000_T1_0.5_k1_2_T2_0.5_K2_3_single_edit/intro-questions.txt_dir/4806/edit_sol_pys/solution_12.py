
import sys

def main():
    data = sys.stdin.readline().strip()[1:-1]
    counter = 0
    for i in range(len(data)):
        if i == len(data) - 1:
            counter += 2
        elif i == len(data) - 2:
            counter += 1
        elif i == 0:
            counter += 1
        else:
            if data[i] == data[i + 1] and data[i + 1] == data[i + 2]:
                counter += 1
            else:
                counter += 2
    print(counter)


if __name__ == "__main__":
    main()
