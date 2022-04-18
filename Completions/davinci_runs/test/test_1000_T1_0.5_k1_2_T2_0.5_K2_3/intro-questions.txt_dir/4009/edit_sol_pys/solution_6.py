
n, x, y = map(int, input().split()) # n, x, y 입력받기
n = list(input()) # 문자열을 리스트로 저장

if n[y] == '0': # y번째 문자가 0이면
    n[y] = '1' # 1로 바꾸기
else:
    n[y] = '0' # y번째 문자가 1이면 0으로 바꾸고
    # y+1번째부터 x번째까지 문자 바꾸기
    for i in range(y+1, x+1):
        if n[i] == '0': # 0이면
            n[i] = '1' # 1로 바꾸고
            break # 반복문 종료
        else:
            n[i] = '0'

print(n.count('0'))
