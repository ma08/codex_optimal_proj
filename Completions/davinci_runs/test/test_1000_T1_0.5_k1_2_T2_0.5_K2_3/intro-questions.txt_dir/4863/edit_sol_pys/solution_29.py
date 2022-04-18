import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    correct_answers = 0 
    for i in range(n):
        answer = sys.stdin.readline().rstrip()
        if answer == "A":
            correct_answers += 1
    print(correct_answers)

if __name__ == "__main__":
    main()
