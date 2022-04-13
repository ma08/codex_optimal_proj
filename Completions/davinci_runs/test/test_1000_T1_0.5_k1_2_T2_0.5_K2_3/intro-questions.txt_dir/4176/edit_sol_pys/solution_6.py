

import math 

def main():
    A, B = map(int, input().split()) #AとBを受け取る
    print(A * B // math.gcd(A, B)) #AとBの最小公倍数を出力

if __name__ == '__main__':
    main()
