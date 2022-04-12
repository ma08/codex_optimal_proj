
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0]  # сумма от 0 до i
    for i in a:
        sums.append(sums[-1] + i)
    sums.append(sums[-1])
    blocks = []  # блоки [начало, конец, сумма]
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[2])
    blocks.sort(key=lambda x: x[1])
    res = []  # ответ
    while len(blocks) > 0:
        i = blocks[0][0]  # начало блока
        j = blocks[0][1]  # конец блока
        blocks.pop(0)
        res.append([i, j])  # добавляем блок в ответ
        for k in range(len(blocks)):
            if blocks[k][0] < j:  # если начало блока попадает в наш блок
                blocks.pop(k)
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
