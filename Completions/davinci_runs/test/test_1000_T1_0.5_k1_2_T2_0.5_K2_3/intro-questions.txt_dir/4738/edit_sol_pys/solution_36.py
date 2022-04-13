
import sys

def main():
    string = sys.stdin.readline().strip()
    for i in range(1, len(string)):
        if string[:i] * (len(string) // i) == string: # check if the string is a multiple of a shorter string
            print(i)
            break

main()
