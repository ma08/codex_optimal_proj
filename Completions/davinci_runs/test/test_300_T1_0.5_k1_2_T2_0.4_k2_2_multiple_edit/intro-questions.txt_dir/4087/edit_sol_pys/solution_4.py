

def main():
    a = int(input("Enter a number: ")) # ввод числа
    while True:
        if a % 4 == 0: # проверка на кратность
            print("The nearest number is: ", a) # вывод числа
            break
        else:
            a += 1 # инкремент

if __name__ == '__main__':
    main()
