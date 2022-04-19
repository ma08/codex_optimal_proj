import sys

def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if s[i] != "Z":
            s = s[:i] + chr(ord(s[i]) + n) + s[i+1:]
        else:
            s = s[:i] + chr(ord(s[i]) + n - 26) + s[i+1:]
    print(s)

if __name__ == "__main__":
    main()
