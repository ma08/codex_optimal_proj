

def main():
    n = int(input()) # количество элементов в массиве
    a = [int(x) for x in input().split()] # массив
    sums = [0] # массив префиксных сумм
    for i in a:
        sums.append(sums[-1] + i) # добавляем префиксную сумму в конец массива
    sums.append(sums[-1]) # добавляем в конец массива префиксную сумму всего массива
    blocks = [] # массив блоков
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]]) # добавляем в массив блоков блок с индексами и суммой
    blocks.sort(key=lambda x: x[2])
    blocks.sort(key=lambda x: x[1])
    res = [] # массив результатов
    while len(blocks) > 0:
        i = blocks[0][0]
        j = blocks[0][1]
        blocks.pop(0)
        res.append([i, j])
        for k in range(len(blocks)):
            if blocks[k][0] < j:
                blocks.pop(k)
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
