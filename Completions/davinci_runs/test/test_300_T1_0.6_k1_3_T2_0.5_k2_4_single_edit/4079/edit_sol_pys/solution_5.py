import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '42':
            break
        print(line)
if __name__ == "__main__":
    main()
