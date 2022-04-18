
import sys

def main():
    s = sys.stdin.readline().strip().replace("\n", "")
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) - 1):
            if s[i] != s[j] and s[i] not in s[i + 1:j] and s[j] not in s[i + 1:j]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
