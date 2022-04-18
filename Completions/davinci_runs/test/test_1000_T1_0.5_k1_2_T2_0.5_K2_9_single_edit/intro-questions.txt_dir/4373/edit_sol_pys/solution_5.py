

def main():
    n = int(input()) # 수열의 길이
    a = sorted(list(map(int, input().split()))) # 수열 입력
    day = 1 # 일수
    while day <= n: # 일수가 수열의 길이보다 작거나 같을 때
        if day > a[day-1]: # 일수가 수열의 값보다 클 때
            break # 반복문 종료
        day += 1 # 일수 1씩 증가
    print(day-1) # 일수 출력

if __name__ == '__main__':
    main()
