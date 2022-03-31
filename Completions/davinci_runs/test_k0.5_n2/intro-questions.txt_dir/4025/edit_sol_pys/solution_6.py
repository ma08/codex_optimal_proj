
import sys

def main():
    a,b,c = [int(x) for x in sys.stdin.readline().split()] # a,b,cを配列に格納
    print(min(a+b+c,2*a+2*b,2*a+2*c,2*b+2*c)) # 最小値を出力

if __name__ == '__main__':
    main()
