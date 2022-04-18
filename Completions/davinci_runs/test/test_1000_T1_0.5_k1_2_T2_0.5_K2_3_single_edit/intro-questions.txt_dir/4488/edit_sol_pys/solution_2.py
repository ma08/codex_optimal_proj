
import sys

def main():
    num1 = sys.stdin.readline().rstrip() #문자열을 입력받고 개행문자를 제거한다
    num2 = sys.stdin.readline().rstrip() #문자열을 입력받고 개행문자를 제거한다

    if len(num1) > len(num2): #첫번째 수의 길이가 두번째 수의 길이보다 클 때
        print("GREATER")
    elif len(num1) < len(num2): #첫번째 수의 길이가 두번째 수의 길이보다 작을 때
        print("LESS")
    else:
        for i in range(len(num1)): #첫번째 수의 길이만큼 반복
            if int(num1[i]) > int(num2[i]): #첫번째 수의 i번째 자리 수가 두번째 수의 i번째 자리 수보다 클 때
                print("GREATER")
                break
            elif int(num1[i]) < int(num2[i]): #첫번째 수의 i번째 자리 수가 두번째 수의 i번째 자리 수보다 작을 때
                print("LESS")
                break
            else:
                if i == len(num1)-1: #마지막 자리까지 반복했을 때
                    print("EQUAL")

if __name__ == '__main__':
    main()
