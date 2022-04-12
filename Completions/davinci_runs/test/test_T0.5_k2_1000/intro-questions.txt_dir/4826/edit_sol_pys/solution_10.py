
import sys

def who_wins(n): # function to find the winner
    if n % 2 == 1:
        return "Alice"
    else:
        return "Bob"

def main():
    n = int(sys.stdin.readline().strip())
    print(who_wins(n))

if __name__ == '__main__':
    main()
