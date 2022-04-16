

from sys import stdin

def main():
    n = int(stdin.readline().strip())
    passwords = [stdin.readline().strip().split(' ') for _ in range(n)]
    passwords.sort(key=lambda x: x[1], reverse=True)
    sm = 0
    for i in range(n):
        sm += (i+1)*float(passwords[i][1])
    print(sm)

if __name__ == '__main__':
    main()
