
import math

def main():
    N = int(input())
    S = input()
    print(S[:N//2] + S[N//2+1:])

if __name__ == '__main__':
    main()
