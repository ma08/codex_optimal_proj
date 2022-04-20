
import sys
def main():
    if len(sys.argv) < 2:
        print("Please provide a filename")
        return
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            n, k = map(int, line.split())
            t = input()
            print(t*(k//n) + t[:k%n])

if __name__ == "__main__":
    main()
