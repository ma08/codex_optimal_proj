
import sys

def main():
    line = sys.stdin.readline()
    line = line.strip()
    print(line[0], end="")
    for i in range(len(line)):
        if line[i] == "-":
            print(line[i+1], end="")

if __name__ == "__main__":
    main()
