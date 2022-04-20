
import sys

def main():
    S = sys.stdin.readline()
    S = S.strip()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

if __name__ == '__main__':
    main()