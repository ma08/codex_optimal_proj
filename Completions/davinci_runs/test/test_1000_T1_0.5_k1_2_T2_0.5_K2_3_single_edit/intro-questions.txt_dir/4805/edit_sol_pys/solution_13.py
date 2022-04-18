
import sys

def main():
    words = [word for word in sys.stdin.readline().strip().split()] # list of words
    if len(words) == len(set(words)):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
