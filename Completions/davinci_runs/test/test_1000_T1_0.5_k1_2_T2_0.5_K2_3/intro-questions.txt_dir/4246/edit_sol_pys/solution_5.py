import sys

def main():
    forecast = sys.stdin.readline()
    actual = sys.stdin.readline()

    correct = 0
    for i in range(len(forecast.strip())):
        if forecast.strip()[i] == actual.strip()[i]:
            correct += 1
    print(correct)

if __name__ == '__main__':
    main()
