import sys

def main():
    string = sys.stdin.readline().strip()
    for i in range(1, len(string)):
        if string[:i] * (len(string) // i) == string:
            print(i)
            break
