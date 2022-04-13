

def main():
    n = int(input())
    t = list(map(int, input().split()))  # Выделяем элементы из строки в список
    t.sort()
    for i in range(n // 2):
        t[i], t[n - 1 - i] = t[n - 1 - i], t[i]

    print(*t)

if __name__ == "__main__":
    main()
