
import sys

def main():
    n = int(sys.stdin.readline().strip())  # read the number of lines
    lines = []
    for i in range(n):  # read the lines
        lines.append(sys.stdin.readline().strip().split())
    for i in range(n):  # check if the first word is in the rest of the line
        for j in range(i):
            if lines[j][-1] in lines[i][:-2]:
                continue
            else:
                print(i + 1)
                return

    print("correct")

if __name__ == "__main__":
    main()
