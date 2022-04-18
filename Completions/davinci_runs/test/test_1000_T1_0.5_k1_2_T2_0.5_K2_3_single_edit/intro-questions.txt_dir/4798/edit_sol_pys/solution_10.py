


import sys

def main():
    line = sys.stdin.readline()
    line = line.strip()
    sys.stdout.write(line[0])
    for i in range(len(line)):
        if line[i] == "-":
            sys.stdout.write(line[i+1])

if __name__ == "__main__":
    main()
