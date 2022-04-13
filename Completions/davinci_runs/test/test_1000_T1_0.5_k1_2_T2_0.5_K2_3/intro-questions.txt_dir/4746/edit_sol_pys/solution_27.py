import sys

def main():
    capacity, num_stations = map(int, sys.stdin.readline().split())
    for i in range(num_stations):
        left, entered, waiting = map(int, sys.stdin.readline().split()) # read in data
        if i == 0:
            people = left
        else:
            people += entered - left
            if people < 0 or people > capacity or (waiting > 0 and people == capacity): # check if possible
                print("impossible")
                return
    if people > 0: # check if possible
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
