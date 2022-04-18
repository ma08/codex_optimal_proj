

import sys

def main():
    forecast = sys.stdin.readline().strip()
    actual = sys.stdin.readline().strip()

    correct = 0
    for i in range(len(forecast)):
        if forecast[i] == actual[i]:
            correct += 1
    print(correct)

if __name__ == '__main__':
    main()