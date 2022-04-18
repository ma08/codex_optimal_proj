import sys

def main():
    n = int(sys.stdin.readline().strip())
    correct = 0
    for i in range(n):
        answer = sys.stdin.readline().strip()
        if answer == "A":
            correct += 1
    print(correct)

if __name__ == "__main__":
    main()
