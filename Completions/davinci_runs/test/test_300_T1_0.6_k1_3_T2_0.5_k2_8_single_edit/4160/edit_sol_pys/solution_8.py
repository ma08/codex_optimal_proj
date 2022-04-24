

import math

def main():
    x = int(input())

    ans = math.log(x/100, 1.01)
    print(int(math.ceil(ans)))

if __name__ == '__main__':
    main()
