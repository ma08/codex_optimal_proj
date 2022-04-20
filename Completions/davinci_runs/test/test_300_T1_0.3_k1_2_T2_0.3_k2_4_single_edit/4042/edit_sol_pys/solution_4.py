
import sys

def main():
    x = float(sys.stdin.readline())  # вводим дробное число
    a = int(round(x, 0))  # округляем до целого числа
    b = int(round(x * 10, 0)) - a * 10  # округляем до десятых и вычитаем из него округленное до целого
    print(a, b)  # выводим ответ

if __name__ == '__main__':
    main()
