
import sys 

def main():
    s = sys.stdin.readline().strip()
    print('hiss' if 'ss' in s else 'no hiss') 

main()
