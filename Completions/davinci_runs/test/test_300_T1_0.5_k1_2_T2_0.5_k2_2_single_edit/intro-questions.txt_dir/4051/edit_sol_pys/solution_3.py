

def main():
    n = int(input())
    a = list(map(int, input().split())) # получаем список чисел из строки
    m = max(a) # находим максимальное значение
    for i in range(m):
        for j in range(n):
            if a[j] >= m - i: # проверяем, сколько звездочек надо вывести
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print(a)
    print("YES" if sorted(a) == a else "NO")

main()
