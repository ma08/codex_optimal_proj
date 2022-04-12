import sys

def main():
    n = int(sys.stdin.readline().strip())
    correct_answers = 0
    for i in range(n):
        answer = sys.stdin.readline().strip()
        if answer == "A":
            correct_answers += 1
    print(correct_answers)

if __name__ == "__main__":
    main()
