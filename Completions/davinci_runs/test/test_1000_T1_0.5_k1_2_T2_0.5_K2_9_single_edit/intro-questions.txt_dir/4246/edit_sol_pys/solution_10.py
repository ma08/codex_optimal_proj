

import sys

def main():
    forecast = sys.stdin.readline().strip().split()
    actual = sys.stdin.readline().strip().split()

    correct = 0
    for i in range(1, len(forecast)):
        if forecast[i] == actual[i-1]:
            correct += 1
    print(correct)

if __name__ == '__main__':
    main()
