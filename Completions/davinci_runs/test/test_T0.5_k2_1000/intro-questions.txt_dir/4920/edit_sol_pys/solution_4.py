import sys

def main():
    s = sys.stdin.readline().strip().lower()
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j] and s[i] not in s[i+1:j] and s[j] not in s[i+1:j]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
