
from datetime import datetime

def main():
    current_time = datetime.strptime(input(), '%H:%M:%S')
    explosion_time = datetime.strptime(input(), '%H:%M')
    explosion_time += (current_time - datetime.strptime('00:00', '%H:%M'))
    print(explosion_time.strftime('%H:%M'))

if __name__ == '__main__':
    main()
