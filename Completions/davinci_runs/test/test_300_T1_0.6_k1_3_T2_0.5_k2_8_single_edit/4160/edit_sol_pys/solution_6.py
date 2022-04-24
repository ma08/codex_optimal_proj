

import math

def main():
    x = input()

    ans = math.log(x/100, 1.01) # I think this is wrong
    print(math.ceil(ans))

if __name__ == '__main__':
    main()
