
import sys

def main():
    N = int(input())
    S = input()
    count = 0
    if N == 1:
        print(1)
    else:
        for i in range(N):
            if i == 0:
                count += 1
            else:
                if S[i] != S[i-1]:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()
