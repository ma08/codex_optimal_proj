

num = int(input())  # количество чисел
input_list = list(map(int, input().split()))  # список чисел
# перебор всех чисел из списка

for i in input_list:
    if i % 2 == 0:  # проверка на четность
        if i % 3 != 0 and i % 5 != 0:  # проверка на делимость на 3 и 5
            print("DENIED")
            exit(0)
print("APPROVED")
