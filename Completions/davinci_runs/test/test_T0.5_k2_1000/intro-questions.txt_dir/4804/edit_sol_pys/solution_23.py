

import sys

def main():
    n = int(sys.stdin.readline().strip())
    print(n,":",end="")
    for i in range(2,n//2+1):  # 從2開始檢查
        if n%i == 0 and n//i-i>=0:  # 如果n%i為0且n//i-i>=0
            print(i,n//i,end="")  # 輸出i和n//i
    for i in range(2,n//2+1):  # 從2開始檢查
        if n%i == 1 and n//i-i>=0:  # 如果n%i為1且n//i-i>=0
            print(i,n//i,end="")  # 輸出i和n//i

if __name__ == '__main__':
    main()
