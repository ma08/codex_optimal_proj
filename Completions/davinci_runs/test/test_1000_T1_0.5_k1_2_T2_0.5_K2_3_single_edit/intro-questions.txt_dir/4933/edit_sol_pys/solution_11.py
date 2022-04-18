
import sys

def main():
    numbers = [int(x) for x in sys.stdin.readline().split()] # read numbers
    numbers.sort()
    diff = numbers[1] - numbers[0] # get difference between first two numbers
    print(numbers[2] + diff) # add difference to the largest number

if __name__ == '__main__':
    main()
