
import sys

def main():
    forecast = sys.stdin.readline().strip().split()
    actual = sys.stdin.readline().strip().split()

    correct = 0
    for i in range(len(forecast) - 1):
        if forecast[i] == actual[i] and forecast[i + 1] == actual[i + 1]:
            correct += 2
    print(correct)

if __name__ == '__main__':
    main()
