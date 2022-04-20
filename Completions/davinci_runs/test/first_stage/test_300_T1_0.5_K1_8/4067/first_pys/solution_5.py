

import sys

def main():
    n = int(input())
    s = input()

    if n % 3 != 0:
        print("n is not divisible by 3")
        sys.exit(1)

    # Count number of characters
    c = {'0': 0, '1': 0, '2': 0}
    for i in range(n):
        c[s[i]] += 1

    # Replace characters to make the string balanced
    for i in range(n):
        if c['0'] > n//3:
            c['0'] -= 1
            c['2'] += 1
            s = s[:i] + '2' + s[i+1:]
        elif c['2'] > n//3:
            c['2'] -= 1
            c['0'] += 1
            s = s[:i] + '0' + s[i+1:]
        elif c['1'] > n//3:
            c['1'] -= 1
            c['2'] += 1
            s = s[:i] + '2' + s[i+1:]

    print(s)

if __name__ == "__main__":
    main()