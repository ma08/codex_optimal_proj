import sys

def main():
    s = sys.stdin.readline().rstrip()
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
