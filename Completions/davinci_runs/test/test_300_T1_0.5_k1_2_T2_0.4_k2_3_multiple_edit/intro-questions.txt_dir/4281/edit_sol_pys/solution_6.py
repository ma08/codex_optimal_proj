

# min_cnt: 같은 숫자가 연속되는 경우 하나로 카운트

# 개선점: 입력받은 문자열을 그대로 저장하고 뒤의 값과 비교하는 방식으로 변경
# max_cnt: 같은 숫자가 연속되는 경우 각각 카운트

n = int(input())
x = [int(i) for i in input().split()]

#print(n, x)

min_cnt = 0
max_cnt = 0

def min_cnt_calc(x):
    curr = x[0]
    min_cnt = 1
    for i in range(1, len(x)):
        if x[i] != curr:
            curr = x[i]
            min_cnt += 1
    return min_cnt

def max_cnt_calc(x):
    curr = x[0]
    max_cnt = 1
    for i in range(1, len(x)):
        if x[i] != curr:
            curr = x[i]
            max_cnt += 1
        elif x[i] == curr and i == len(x)-1:
            max_cnt += 1
    return max_cnt

print(min_cnt_calc(x), max_cnt_calc(x))
