

import math

def main():
    a,b,c = map(int, input().split())
    print(min(a,b,c) + math.ceil((a+b+c)/5))

if __name__ == "__main__":
    main()