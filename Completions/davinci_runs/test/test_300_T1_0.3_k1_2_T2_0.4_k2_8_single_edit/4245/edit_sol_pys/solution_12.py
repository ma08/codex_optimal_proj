import sys

def main():
    line = sys.stdin.readline().rstrip()
    A, B = map(int, line.split())
    print(B // A + (B % A != 0))
