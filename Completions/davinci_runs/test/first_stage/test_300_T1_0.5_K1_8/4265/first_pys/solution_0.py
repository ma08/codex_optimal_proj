

from sys import stdin

def main():
    s = stdin.readline().strip()
    t = stdin.readline().strip()
    print(sum(s[i] != t[i] for i in range(len(s))))

if __name__ == "__main__":
    main()