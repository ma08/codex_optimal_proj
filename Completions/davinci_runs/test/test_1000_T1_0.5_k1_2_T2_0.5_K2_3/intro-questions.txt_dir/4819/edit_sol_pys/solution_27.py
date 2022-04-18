
import sys

def main():
    modulo = 42
    numbers = []
    for i in range(10):
        numbers.append(int(input()) % modulo)

    print(len(set(numbers)))


if __name__ == '__main__':
    sys.exit(main())
