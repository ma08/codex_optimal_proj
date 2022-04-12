import sys

def main():
    n = int(input())
    correct = 0
    for i in range(n):
        answer = input()
        if answer == "A" or answer == "a":
            correct += 1
    print(correct)

if __name__ == "__main__":
    main()
