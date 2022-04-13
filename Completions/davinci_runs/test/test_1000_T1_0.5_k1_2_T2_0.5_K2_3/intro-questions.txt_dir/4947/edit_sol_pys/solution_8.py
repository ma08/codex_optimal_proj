

import math

def main():
    x = float(input()) #input the number of feet
    print(int(math.ceil(x * 0.3048))) #convert feet to meters

if __name__ == "__main__":
    main()
