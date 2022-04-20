

import math

def main():
    # Read Input
    x, y = map(int, input().split())

    # Calc
    ans = math.ceil(math.log(y/x, 1.01))

    # Print Answer
    print(ans if ans <= 40 else 'impossible')

if __name__ == '__main__':
    main()
