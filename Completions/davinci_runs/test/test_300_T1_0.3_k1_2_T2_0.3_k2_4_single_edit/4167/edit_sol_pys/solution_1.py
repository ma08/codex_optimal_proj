

import math

def main():
    N,K = map(int, input().split())
    print(math.ceil(N/K)*math.ceil(N/K)*math.ceil(N/K)) # 切り上げ

if __name__ == '__main__':
    main()
