import sys

def main():
    K = int(sys.stdin.readline().strip())
    desks = [int(sys.stdin.readline().strip()) for _ in range(K)]
    count = 0
    for i in range(K):
        count += 1
        if desks[i] < i + 1:
            count += i + 1 - desks[i]
    print(count)

if __name__ == '__main__':
    main()
