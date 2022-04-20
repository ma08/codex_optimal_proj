


def median(numbers):
    num = sorted(numbers)
    if len(num) % 2 == 0:
        med = num[len(num) // 2] + num[len(num) // 2 - 1]
        return med
    return num[len(num) // 2]


def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n + 1):
            if median(seq[i:j]) == m:
                c += 1 
    print(c)


if __name__ == '__main__':
    main() 
