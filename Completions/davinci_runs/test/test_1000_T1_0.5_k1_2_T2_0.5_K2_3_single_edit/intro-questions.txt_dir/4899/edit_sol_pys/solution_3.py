
import sys

def main():
    greeting = sys.stdin.readline().strip()
    new_greeting = greeting.replace('e', 'ee', 1) #replace the first 'e' with 'ee'
    print(new_greeting)


if __name__ == '__main__':
    main()
