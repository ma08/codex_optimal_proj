

import sys

def is_launch_window(year):
  if year % 26 == 2:
    return 'yes'
  else:
    return 'no'

if __name__ == '__main__':
  print(is_launch_window(int(sys.stdin.readline())))
