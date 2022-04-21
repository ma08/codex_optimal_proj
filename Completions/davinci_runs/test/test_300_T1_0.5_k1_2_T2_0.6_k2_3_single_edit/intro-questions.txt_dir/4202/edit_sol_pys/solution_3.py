import sys

def main():
    L, R = map(int, sys.stdin.readline().split())

    if R - L >= 2020:
        print(0)
    else:
        min_val = 2021
        for i in range(L, R):
            for j in range(i+1, R+1):
                min_val = min(min_val, (i*j) % 2020)
        print(min_val)

if __name__ == '__main__':
    main()
