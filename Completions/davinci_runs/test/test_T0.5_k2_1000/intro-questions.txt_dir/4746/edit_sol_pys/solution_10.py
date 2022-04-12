import sys

def main():
    for line in sys.stdin:
        capacity, num_stations = map(int, line.split())
        for i in range(num_stations):
            left, entered, waiting = map(int, sys.stdin.readline().split())
            if i == 0:
                people = left
            else:
                people += entered - left
                if people < 0 or people > capacity or (waiting > 0 and people == capacity):
                    print("impossible")
                    return
        if people > 0:
            print("impossible")
        else:
            print("possible")

if __name__ == '__main__':
    main()
