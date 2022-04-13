import sys
import os
import re

def main():
    file_name = sys.argv[1]
    with open(file_name) as f:
        n = int(f.readline())
        correct_answers = 0
        for i in range(n):
            answer = f.readline()
            if answer == "A\n":
                correct_answers += 1
        print(correct_answers)

if __name__ == "__main__":
    main()
