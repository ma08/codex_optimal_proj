

import math

def solution(n):
    
    # 제곱근 구하기
    sqrt = int(math.sqrt(n))
    
    # 결과값 초기화
    answer = 0
    
    for i in range(1, sqrt+1):
        # 제곱수면 카운트 +1
        if i * i == n:
            answer += 1
        # 제곱수가 아니면 그냥 넘어감
        elif i * i < n:
            pass
        # 제곱수가 아니면 반복문 종료
        else:
            break
    
    return answer

# print(solution(11))
# print(solution(14))
# print(solution(61441))
print(solution(571576))
# print(solution(2128506))