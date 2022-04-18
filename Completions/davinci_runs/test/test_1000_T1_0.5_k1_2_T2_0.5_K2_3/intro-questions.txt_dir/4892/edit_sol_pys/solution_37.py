

from sys import stdin


def main():
    n = int(stdin.readline().strip())
    passwords = [stdin.readline().strip().split(' ') for _ in range(n)]
    passwords.sort(key=lambda x: x[1], reverse=True)
    total = 0
    for i in range(n):
        total += (i+1)*float(passwords[i][1])
    print(total)

if __name__ == '__main__':
    main()
