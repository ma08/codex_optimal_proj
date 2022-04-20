

S, W = map(int, input().split())  # 강수량과 습도를 입력받아서 변수에 저장
if(W >= S):  # 습도가 강수량보다 크거나 같을 때
    print("unsafe")
else:  # 습도가 강수량보다 작을 때
    print("safe")
