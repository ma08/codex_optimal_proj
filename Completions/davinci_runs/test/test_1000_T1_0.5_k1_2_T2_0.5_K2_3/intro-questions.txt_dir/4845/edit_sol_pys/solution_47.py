

d, m = map(int, input().split())  # принимаем дату и месяц

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # количество дней в месяцах
day = sum(days[:m]) + d  # подсчитываем сколько дней прошло с начала года
day %= 7  # получаем номер дня недели

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')  # названия дней недели
print(days_of_the_week[day])  # выводим название дня недели по номеру дня недели
