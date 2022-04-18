
x = int(input())  # вводим число

time = 0
while x > 0:  # уменьшаем число на количество шагов
    time += 1
    x -= time

print(time)  # выводим количество шагов
