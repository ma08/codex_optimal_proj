
import sys

def main():
    line = sys.stdin.readline().strip()
    words = line.split()
    if len(words) == len(set(words)) and line == " ".join(words):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
