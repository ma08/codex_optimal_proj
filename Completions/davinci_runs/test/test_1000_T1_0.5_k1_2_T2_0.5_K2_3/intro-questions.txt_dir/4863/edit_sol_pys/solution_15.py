
import sys


def main():
    n = int(sys.stdin.readline())
    incorrect = 0
    for i in range(n):
        answer = sys.stdin.readline().strip()
        if answer != "A":
            incorrect += 1
    print(incorrect)


if __name__ == "__main__":
    main()
