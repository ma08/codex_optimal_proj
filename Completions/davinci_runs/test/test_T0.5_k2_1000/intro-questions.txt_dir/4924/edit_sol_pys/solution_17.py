

from datetime import datetime

def main():
    current_time = datetime.strptime(input(), '%H:%M:%S')
    explosion_time = datetime.strptime(input(), '%H:%M:%S') + (current_time - datetime.strptime('00:00:00', '%H:%M:%S')) + datetime.strptime('00:00:00', '%H:%M:%S')
    print(explosion_time.strftime('%X'))

if __name__ == '__main__':
    main()
