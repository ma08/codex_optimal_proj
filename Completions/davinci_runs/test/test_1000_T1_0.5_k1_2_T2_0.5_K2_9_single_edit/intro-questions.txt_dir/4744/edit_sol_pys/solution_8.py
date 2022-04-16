
import math

def main():
    V = int(input('Enter a number: '))
    # Find the smallest integer that is a factor of V
    for i in range(2, int(math.sqrt(V)) + 1):
        if V % i == 0:
            # The cost of the box is the perimeter of the rectangle
            print('The smallest integer that is a factor of V is: ', 2 * (V // i + i))
            break

if __name__ == "__main__":
    main()
