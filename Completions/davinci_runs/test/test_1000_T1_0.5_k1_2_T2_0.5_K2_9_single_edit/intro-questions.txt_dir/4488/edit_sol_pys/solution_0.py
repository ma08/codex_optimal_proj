
import sys

def main():
    num1 = sys.stdin.readline().rstrip() # readline()은 \n까지 포함해서 읽어오기 때문에 rstrip()으로 \n을 제거한다.
    num2 = sys.stdin.readline().rstrip() # readline()은 \n까지 포함해서 읽어오기 때문에 rstrip()으로 \n을 제거한다.

    if len(num1) > len(num2): # 첫번째 수의 길이가 더 길면 GREATER
        print("GREATER")
    elif len(num1) < len(num2): # 두번째 수의 길이가 더 길면 LESS
        print("LESS")
    else:
        for i in range(len(num1)): # 길이가 같으면 각 자리수를 비교한다.
            if int(num1[i]) > int(num2[i]): # 첫번째 수의 자리수가 더 크면 GREATER
                print("GREATER")
                break
            elif int(num1[i]) < int(num2[i]): # 두번째 수의 자리수가 더 크면 LESS
                print("LESS")
                break
            else: # 자리수가 같으면 다음 자리수로 넘어간다.
                if i == len(num1)-1: # 모든 자리수를 비교해보았는데도 아무것도 안나오면 EQUAL
                    print("EQUAL")

if __name__ == '__main__':
    main()
