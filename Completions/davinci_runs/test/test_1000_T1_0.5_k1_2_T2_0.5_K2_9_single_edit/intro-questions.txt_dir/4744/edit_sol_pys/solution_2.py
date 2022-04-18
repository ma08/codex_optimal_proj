

import math

def main():
    V = int(input())
    # Find the smallest integer that is a factor of V
    while True:
        if V % 2 == 0:
            V = V / 2
        else:
            break
    print(int(V))
    

if __name__ == "__main__":
    main()
