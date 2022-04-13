


import sys

def main():
    # Reading input
    a = [int(x) for x in sys.stdin.readline().split()]

    # Computing and printing answer
    print(min(a))
    
if __name__ == '__main__':
    main()
