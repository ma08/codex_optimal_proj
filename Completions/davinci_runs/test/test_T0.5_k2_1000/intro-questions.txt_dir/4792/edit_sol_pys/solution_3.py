
import sys

def main():
    string = sys.stdin.readline().strip()
    compact = string[0]
    for i in range(1, len(string)):
        if string[i] != compact[-1]:
            compact += string[i]
    print(compact) 

main()
