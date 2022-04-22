#!/usr/bin/python3

import sys

def main():
  n = int(sys.stdin.readline()) # read the number
  num = n
  while True: # loop
    if num % 2 == 0:
      print(num)
      break
    num += n

if __name__ == '__main__':
  main()
