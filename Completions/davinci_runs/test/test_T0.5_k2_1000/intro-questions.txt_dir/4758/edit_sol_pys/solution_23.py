import sys

def main():
    N,T,M = map(int,sys.stdin.readline().split()) #N:列数、T:時間、M:人数
    print(N*T*M) #出力

if __name__ == "__main__":
    main()
