
import sys

def main():
    for line in sys.stdin:
        data = line.strip()
        print(len(data))

if __name__ == "__main__":
    main()
