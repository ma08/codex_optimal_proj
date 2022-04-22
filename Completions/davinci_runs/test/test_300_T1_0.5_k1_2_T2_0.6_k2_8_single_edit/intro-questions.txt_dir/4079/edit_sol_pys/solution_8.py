

n = int(input())
lst = []
for i in range(n): #цикл для создания массива из ввода пользователя
    lst.append(input()) #добавляем в массив ввод пользователя

for i in lst:
    if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1: # проверяем вхождение в заданные условия
        print("Yes")
    else:
        print("No")
