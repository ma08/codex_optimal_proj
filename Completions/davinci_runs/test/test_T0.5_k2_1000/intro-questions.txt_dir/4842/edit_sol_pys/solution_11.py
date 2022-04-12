
import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = [int(x) for x in sys.stdin.readline().strip().split()] # v[i] is the number of people in the i-th room
    diff = [v[i+1]-v[i] for i in range(n-1)] # diff[i] is the number of people who enter the (i+1)-th room from the i-th room
    while True:
        d = diff[0] # d is the number of people who enter the second room from the first room
        for i in range(1,len(diff)):
            if diff[i] != d:
                break
        else:
            break
        diff = [diff[i+1]-diff[i] for i in range(len(diff)-1)] # diff[i] is the number of people who enter the (i+2)-th room from the (i+1)-th room
    d = v[n-1]+d # d is the number of people who enter the first room from the last room
    print(len(diff), d) # len(diff) is the number of rooms and d is the number of people who enter the first room from the last room

if __name__ == '__main__':
    main()
