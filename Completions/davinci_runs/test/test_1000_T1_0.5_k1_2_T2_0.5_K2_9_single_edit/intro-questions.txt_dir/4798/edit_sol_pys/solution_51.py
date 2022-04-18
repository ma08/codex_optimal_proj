


import sys

def main():
    line = sys.stdin.readline()
    line = line.strip()
    print(line[0])
    for i in range(len(line)):
        if line[i] == "-":
            print(line[i+1])

if __name__ == "__main__":
    main()
