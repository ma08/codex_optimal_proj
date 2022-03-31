
a,b,c,d = map(int,input().split()) # a,b,c,d를 입력받아 int형으로 변환하여 a,b,c,d에 저장

max_value = a*c # 가장 큰 값을 저장할 변수 max_value에 a*c를 저장
if a*d > max_value: # a*d가 max_value보다 크면
    max_value = a*d # max_value에 a*d를 저장
if b*c > max_value: # b*c가 max_value보다 크면
    max_value = b*c # max_value에 b*c를 저장
if b*d > max_value: # b*d가 max_value보다 크면
    max_value = b*d # max_value에 b*d를 저장

print(max_value) # max_value를 출력
