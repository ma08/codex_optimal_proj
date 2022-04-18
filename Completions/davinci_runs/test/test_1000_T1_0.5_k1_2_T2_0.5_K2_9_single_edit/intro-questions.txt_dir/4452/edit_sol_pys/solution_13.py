
import sys

def get_round_numbers(n): # функция возвращает массив округленных чисел
    round_numbers = [] # массив округленных чисел
    num = n
    while num > 0: # пока число не станет равным нулю
        rn = (num // 10) * 10 # округляем число до ближайшего десятка
        round_numbers.append(rn) # добавляем в массив округленное число
        num = num - rn # вычитаем округленное число из исходного
    return round_numbers

def main():
    t = int(sys.stdin.readline().strip()) # считываем количество тестов
    for i in range(t): # проходим по каждому тесту
        n = int(sys.stdin.readline().strip()) # считываем число для которого нужно получить округленные числа
        round_numbers = get_round_numbers(n) # получаем массив округленных чисел
        print(len(round_numbers)) # выводим количество округленных чисел
        print(*round_numbers) # выводим массив округленных чисел

if __name__ == '__main__':
    main()
