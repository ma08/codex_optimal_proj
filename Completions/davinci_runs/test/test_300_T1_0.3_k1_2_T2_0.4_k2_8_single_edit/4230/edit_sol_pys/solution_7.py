
import sys

def main():
    s = sys.stdin.readline().rstrip('\n')
    if s == 'Sunny':
        print('Cloudy')
    elif s == 'Cloudy':
        print('Rainy')
    elif s == 'Rainy':
        print('Sunny')

if __name__ == '__main__':
    main()
