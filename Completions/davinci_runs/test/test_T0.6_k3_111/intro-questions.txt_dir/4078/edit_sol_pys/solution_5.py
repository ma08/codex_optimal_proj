
def read_input():
    n, m = map(int, input().split())  # n - количество элементов в массиве, m - количество отрезков
    a = list(map(int, input().split()))  # массив
    segments = []  # массив отрезков
    for _ in range(m):  # заполняем массив отрезков
        l, r = map(int, input().split())  # левая и правая граница отрезка
        segments.append((l, r))  # добавляем отрезок в массив
    return a, segments  # возвращаем массив и массив отрезков

def solution(a, segments):
    max_in_array = max(a)  # максимальный элемент в массиве
    min_in_array = min(a)  # минимальный элемент в массиве
    d = max_in_array - min_in_array  # максимальная разность в массиве
    q = 0  # количество отрезков с максимальной разностью
    chosen_segments = []  # массив отрезков с максимальной разностью
    for l, r in segments:  # проходим по всем отрезкам
        min_in_segment = min(a[l-1:r])  # минимальный элемент в отрезке
        max_in_segment = max(a[l-1:r])  # максимальный элемент в отрезке
        if max_in_segment - min_in_segment > d:  # если разность в отрезке больше разности в массиве
            q = 1  # количество отрезков с максимальной разностью равно 1
            chosen_segments = [l]  # массив отрезков с максимальной разностью равен отрезку
            d = max_in_segment - min_in_segment  # максимальная разность равна разности в отрезке
        elif max_in_segment - min_in_segment == d:  # если разность в отрезке равна разности в массиве
            q += 1  # увеличиваем количество отрезков с максимальной разностью на 1
            chosen_segments.append(l)  # добавляем отрезок в массив отрезков с максимальной разностью
    print(d)  # выводим максимальную разность
    print(q)  # выводим количество отрезков с максимальной разностью
    print(*chosen_segments)  # выводим массив отрезков с максимальной разностью

if __name__ == "__main__":
    a, segments = read_input()
    solution(a, segments)
