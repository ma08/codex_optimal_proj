
import sys

def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    s = ''.join(s)
    t = ''.join(t)
    print('Yes' if s < t else 'No')

if __name__ == "__main__":
    main()
