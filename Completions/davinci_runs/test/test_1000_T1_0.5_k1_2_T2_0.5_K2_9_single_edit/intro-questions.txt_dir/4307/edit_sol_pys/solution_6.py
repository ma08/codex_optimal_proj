

N = int(input()) #N개의 수
num = list(map(int, input().split())) #N개의 수를 입력받는다
num.sort() #오름차순으로 정렬
print(num[N//2]) #정렬한 값의 중간 값을 출력
