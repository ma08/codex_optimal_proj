import sys

def main():
    n, k, q = map(int, sys.stdin.readline().split())
    scores = [k] * n
    for _ in range(q):
        answer = int(sys.stdin.readline().rstrip())
        scores[answer - 1] += 1
        for i in range(n):
            if i == answer - 1:
                continue
            scores[i] -= 1

    for s in scores:
        if s > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
