
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split()) # a,b,c,d가 들어오면 정수형으로 바꿔줌
    count = 0

    for i in range(a, b + 1):
        if i % c != 0 and i % d != 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
