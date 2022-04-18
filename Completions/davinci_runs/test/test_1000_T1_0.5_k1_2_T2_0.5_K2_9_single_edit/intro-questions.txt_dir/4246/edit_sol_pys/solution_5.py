
import sys

def main():
    forecast = sys.stdin.readline().strip().split()
    actual = sys.stdin.readline().strip().split()

    correct = 0.0
    wrong = 0.0
    for i in range(len(forecast)):
        if forecast[i] == actual[i] and actual[i] == '1':
            correct += 1
        elif forecast[i] != actual[i] and actual[i] == '0':
            correct += 1
        else:
            wrong += 1

    print(correct / (correct + wrong))

if __name__ == '__main__':
    main()
