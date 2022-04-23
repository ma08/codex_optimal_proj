import math

def main():
    n = int(input())  # number of test cases
    for i in range(n):
        s = input()
        count = 0
        for i in range(len(s)):
            if s[i] == '4':
                count += 1
        print(count)

if __name__ == '__main__':
    main()
