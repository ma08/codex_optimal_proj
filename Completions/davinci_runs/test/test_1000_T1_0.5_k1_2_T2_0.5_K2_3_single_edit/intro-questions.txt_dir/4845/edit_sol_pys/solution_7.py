

d, m = map(int, input().split())  # получаем день и месяц в виде чисел

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # количество дней в месяцах
day = sum(days[:m]) + d  # получаем номер дня в году
day %= 7  # делим на 7 и получаем день недели

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days_of_week[day])
