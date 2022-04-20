

# Write your code here
a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))

if a % 2 == 0:
    for i in range(a):
        print("* " * b)
else:
    for i in range(a):
        if i % 2 == 0:
            print("* " * b)
        else:
            print(" *" * b)
