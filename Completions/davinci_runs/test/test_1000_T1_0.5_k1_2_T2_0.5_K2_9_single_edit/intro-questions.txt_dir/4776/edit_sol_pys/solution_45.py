
import sys

def main():
    data = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]
    for row in data:
        for col in row:
            print(col, end='')
        print()

if __name__ == "__main__":
    main()
