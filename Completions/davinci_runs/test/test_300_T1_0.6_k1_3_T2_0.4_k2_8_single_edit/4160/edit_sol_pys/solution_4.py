

import math

def main():
    x = int(input())

    ans = math.log(x/100, 1.01) 
    print(math.ceil(ans))

if __name__ == '__main__':
    main()
