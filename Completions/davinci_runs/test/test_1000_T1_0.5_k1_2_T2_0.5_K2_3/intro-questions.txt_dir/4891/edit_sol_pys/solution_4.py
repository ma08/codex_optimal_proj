# file

pieces = [1, 1, 2, 2, 2, 8] # количество фигур в шахматной доске
count = [int(i) for i in input().split()] # количество фигур на входной доске

for i in range(6): # вывод на экран разницы количества фигур на шахматной доске и входной доске
    print(pieces[i] - count[i], end=" ")
