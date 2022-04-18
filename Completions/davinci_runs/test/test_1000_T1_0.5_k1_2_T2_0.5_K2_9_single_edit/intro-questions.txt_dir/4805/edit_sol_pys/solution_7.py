
import sys

def main():
    words = [word for word in sys.stdin.readline().strip().split()] 
    print("yes" if len(words) == len(set(words)) else "no")

if __name__ == "__main__":
    main()
