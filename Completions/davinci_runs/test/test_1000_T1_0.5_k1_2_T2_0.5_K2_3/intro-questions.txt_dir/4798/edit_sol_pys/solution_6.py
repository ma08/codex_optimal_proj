import sys

def main():
    line = sys.stdin.readline()
    line = line.strip()
    print(line[0], end=" ")
    for i in range(1, len(line)):
        if line[i-1] == "-":
            print(line[i], end=" ")

if __name__ == "__main__":
    main()
