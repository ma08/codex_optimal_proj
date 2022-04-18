import sys

def main():
    n = int(sys.stdin.readline())
    correct = 0
    for i in range(n):
        answer = sys.stdin.readline().strip()
        if answer == "A\n":
            correct += 1
    print(str(correct))

if __name__ == "__main__":
    main()
