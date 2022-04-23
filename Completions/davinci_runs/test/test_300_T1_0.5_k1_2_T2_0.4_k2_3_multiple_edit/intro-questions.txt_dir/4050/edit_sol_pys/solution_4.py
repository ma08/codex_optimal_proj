

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0]  # массив сумм префиксов
    for i in a:
        sums.append(sums[-1] + i)
    sums.append(sums[-1])
    blocks = []  # массив блоков
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[2])  # сортируем по сумме
    blocks.sort(key=lambda x: x[1])  # сортируем по правой границе
    res = []  # массив ответа
    while len(blocks) > 0:
        i = blocks[0][0]
        j = blocks[0][1]
        blocks.pop(0)
        res.append([i, j])  # добавляем блок в ответ
        for k in range(len(blocks)):
            if blocks[k][0] < j:
                blocks.pop(k)  # удаляем все блоки, которые пересекаются с текущим
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])


main()
