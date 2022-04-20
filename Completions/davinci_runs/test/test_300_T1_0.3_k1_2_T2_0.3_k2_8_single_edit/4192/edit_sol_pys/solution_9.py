
import sys

def main():
    d, t, s = map(int, sys.stdin.readline().split()) # d = distance, t = time, s = speed
    if d / s <= t: # if distance / speed is less than or equal to time
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
