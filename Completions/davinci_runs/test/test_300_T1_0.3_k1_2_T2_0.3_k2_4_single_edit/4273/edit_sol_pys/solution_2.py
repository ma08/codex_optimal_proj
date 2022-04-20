
import sys

def main():
    S = input()
    T = input()
    if S[0] == T[2] and S[1] == T[1] and S[2] == T[0]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
