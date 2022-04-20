

import math

def main():
    # Read Input
    N = int(input())

    # Calc
    ans = math.ceil(math.log(N/100, 1.01))

    # Print Answer
    print(ans)

if __name__ == '__main__':
    main()
