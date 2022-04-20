

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = [0] * n
    for i in range(n):
        answer[(a[i] - b[i]) % n] += 1
    print(' '.join(map(str, answer)))

if __name__ == '__main__':
    main()