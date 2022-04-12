import sys

def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    e.sort(reverse=True)
    count = 0
    for i in e:
        if a >= i:
            count += 1
            a -= i
    print(count)

if __name__ == '__main__':
    main()
