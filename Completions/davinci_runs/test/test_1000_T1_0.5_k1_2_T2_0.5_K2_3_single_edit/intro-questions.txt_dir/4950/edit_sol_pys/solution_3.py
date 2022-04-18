
import sys

def main():
    n = int(sys.stdin.readline())
    times = [None] * n
    distances = [None] * n
    for i in range(n):
        times[i], distances[i] = [int(x) for x in sys.stdin.readline().split()] # чтение входных данных

    max_speed = 0 # максимальная скорость
    for i in range(n):
        for j in range(i+1, n):
            time_diff = times[j] - times[i]
            dist_diff = distances[j] - distances[i]
            speed = dist_diff / time_diff
            if speed > max_speed: # проверка на максимальную скорость
                max_speed = speed

    print(max_speed)

if __name__ == '__main__':
    main()
