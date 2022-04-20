
import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    s_len = len(s)
    for i in range(s_len):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[:-1]
    print("No")

if __name__ == '__main__':
    main()