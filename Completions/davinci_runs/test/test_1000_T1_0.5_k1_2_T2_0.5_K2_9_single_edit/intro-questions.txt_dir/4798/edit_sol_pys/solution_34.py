


import sys

def main():
    line = sys.stdin.readline()
    line = line.strip()
    print(line[0], end="")
    for i in range(len(line)):
        if line[i] == "-" and i != len(line) - 1:
            print(line[i+1], end="")

if __name__ == "__main__":
    main()
