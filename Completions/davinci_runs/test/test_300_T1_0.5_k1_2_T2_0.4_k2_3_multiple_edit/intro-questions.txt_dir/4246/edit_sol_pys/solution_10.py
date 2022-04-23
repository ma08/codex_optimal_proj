
import sys

def main():
    forecast = sys.stdin.readline().strip().split()  # list of strings
    actual = sys.stdin.readline().strip().split()  # list of strings

    correct = 0  # int
    for i in range(len(forecast)):
        if forecast[i] == actual[i]:

            correct += 1
    print(correct)

if __name__ == '__main__':
    main()
