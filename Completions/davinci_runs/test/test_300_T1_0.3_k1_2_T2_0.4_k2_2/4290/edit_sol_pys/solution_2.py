

N, M = map(int, input().split()) #split() 함수는 공백을 기준으로 문자열을 나눠준다.

print((N+M)*(N+M-1)//2 - N*M) #//는 몫을 구하는 함수
