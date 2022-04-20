

def main():
    n = int(input())  # количество слов
    words = input().split()
    d = {}  # словарь для хранения слов
    for i in range(n):
        if words[i] in d:  # если слово уже есть в словаре
            d[words[i]] += 1
        else:  # если слова нет в словаре
            d[words[i]] = 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)  # сортировка слов по частоте
    prev = -1
    res = 0  # длина нового слова
    for i in range(len(d)):
        if d[i][1] != prev:  # если частота не равна предыдущей
            res += len(d[i][0])
            prev = d[i][1]
        else:  # если частота равна предыдущей
            res += 1
    print(res)

if __name__ == "__main__":
    main()
