
n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicates(a):
    b = [] # Создаем новый пустой список
    for i in range(len(a)):
        if a[i] in b: # Если элемент списка дублируется, то пропускаем итерацию
            continue
        else:
            b.append(a[i]) # Если элемент списка не дублируется, то добавляем его в новый список
    return b

b = remove_duplicates(a) # Получаем из функции список с удаленными дубликатами
print(len(b))
print(*b)
