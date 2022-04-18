
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = 2
    for i in range(1, n):
        if a[i-1] + 1 == a[i]:  # 가장 짧은 길이를 찾는 문제.
            result += 1
    print(result)

if __name__ == "__main__":
    main()
