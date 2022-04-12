
from datetime import datetime

def main():
    current_time = datetime.strptime(input(), '%H:%M:%S')  # часы:минуты:секунды
    explosion_time = datetime.strptime(input(), '%H:%M:%S')  # часы:минуты:секунды
    explosion_time += (current_time - datetime.strptime('00:00:00', '%H:%M:%S'))  # прибавляем к времени взрыва
    # время от начала дня до текущего момента
    print(explosion_time.strftime('%H:%M:%S'))  # выводим время взрыва в формате часы:минуты:секунды

if __name__ == '__main__':
    main()
