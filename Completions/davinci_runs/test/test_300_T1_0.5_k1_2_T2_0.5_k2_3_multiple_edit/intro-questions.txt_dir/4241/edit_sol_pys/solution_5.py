"""
Напишите функцию min_changes(first_str, second_str), возвращающую минимальное
количество операций замены одного символа на другой, для того, чтобы получить
из first_str строку second_str. Операции замены можно производить только один раз.
"""

def min_changes(first_str, second_str):
    count = 0
    for i in range(len(first_str)):
        if first_str[i] != second_str[i]:
            count += 1
    return count

def main():
    first_str = input()
    second_str = input()
    print(min_changes(first_str, second_str))

if __name__ == '__main__':
    main()
