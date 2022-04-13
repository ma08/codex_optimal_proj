import sys

def main():
    capacity, num_stations = map(int, sys.stdin.readline().split()) # get capacity and num_stations
    for i in range(num_stations):
        left, entered, waiting = map(int, sys.stdin.readline().split()) # get left, entered, waiting
        if i == 0:
            people = left # at first station
        else:
            people += entered - left # calculate people
            if people < 0 or people > capacity or (waiting > 0 and people == capacity): # if impossible
                print("impossible")
                return
    if people > 0: # if impossible
        print("impossible")
    else: # if possible
        print("possible")

if __name__ == '__main__':
    main()
