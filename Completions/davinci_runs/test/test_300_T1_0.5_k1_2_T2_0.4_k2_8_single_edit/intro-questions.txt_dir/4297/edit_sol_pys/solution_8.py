
import sys

def main(n):
    num = n
    while True:
        if num % 2 == 0:
            print(num)
            break
        num += n

if __name__ == '__main__':
  main()
