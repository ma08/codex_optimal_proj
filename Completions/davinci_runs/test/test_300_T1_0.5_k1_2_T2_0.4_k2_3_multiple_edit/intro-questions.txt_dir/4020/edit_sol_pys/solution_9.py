import sys

def time_to_minutes(time):
    return time[0] * 60 + time[1]

def minutes_to_time(minutes):
    return [minutes // 60, minutes % 60]

def main():
    start_time = [int(x) for x in sys.stdin.readline().split(':')]  # получаем время начала
    end_time = [int(x) for x in sys.stdin.readline().split(':')]  # получаем время конца
    start_minutes = time_to_minutes(start_time)  # переводим время начала в минуты
    end_minutes = time_to_minutes(end_time)  # переводим время конца в минуты
    middle_minutes = (start_minutes + end_minutes) // 2  # считаем среднее время в минутах
    middle_time = minutes_to_time(middle_minutes)  # переводим среднее время в часы и минуты
    print('{:02d}:{:02d}'.format(middle_time[0], middle_time[1]))  # выводим среднее время

if __name__ == '__main__':
    main()
