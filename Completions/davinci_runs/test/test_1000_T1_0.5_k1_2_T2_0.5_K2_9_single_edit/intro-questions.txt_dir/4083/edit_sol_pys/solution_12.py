 
import sys

def main():
 
    n = int(input())
    s = input()
 
    count_a = s.count('A')
    count_b = s.count('B')
 
    if count_a > count_b:
        print('Anton')
    elif count_a < count_b:
        print('Danik')
    else:
        print('Friendship')
 
if __name__ == '__main__':
    main() 
