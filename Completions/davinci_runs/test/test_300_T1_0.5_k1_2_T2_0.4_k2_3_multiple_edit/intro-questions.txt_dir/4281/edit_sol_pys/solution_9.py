

# min_cnt: 같은 숫자가 연속되는 경우 하나로 카운트 (색칠하는 경우)
# max_cnt: 같은 숫자가 연속되는 경우 각각 카운트 (색칠하는 경우)


# x는 숫자들을 입력받은 리스트
n = int(input())
x = [int(i) for i in input().split()]

#print(n, x) # 테스트용

min_cnt = 0
max_cnt = 0

# curr: 현재 숫자
# min
curr = x[0]
min_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_cnt += 1

# max_cnt
# curr: 현재 숫자
curr = x[0]
max_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        max_cnt += 1
    # 마지막 숫자의 경우 카운트하기 위함
    elif x[i] == curr and i == len(x)-1:
        max_cnt += 1

print(min_cnt, max_cnt)
