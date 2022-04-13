
x = int(input().split()[0])  # number
n = int(input().split()[0])  # amount of numbers
p = [int(i) for i in input().split()]  # array
p.sort()

if x <= p[0]:  # if number is less than the smallest number in array, then the difference is smallest and our number
    print(p[0]-x)
elif x >= p[-1]:  # если больше максимального, то разность максимального и нашего
    print(x-p[-1])
else:  # иначе разность между ближайшими числами
    for i in range(1, n):  # проходим по всем числам
        if x <= p[i]:
            print(min(x-p[i-1], p[i]-x))
            break
