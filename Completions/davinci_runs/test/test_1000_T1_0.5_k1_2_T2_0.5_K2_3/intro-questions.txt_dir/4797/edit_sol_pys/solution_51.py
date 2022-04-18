import sys

def main():
    s = sys.stdin.readline().rstrip()
    print(s.replace("<", "").replace(">", ""))

if __name__ == "__main__":
    main()
