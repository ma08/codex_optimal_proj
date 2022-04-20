

S, W = map(int, input().split()) # S=체력, W=무게
if(W >= S): # 무게가 체력보다 크거나 같으면
    print("unsafe") # 안전하지 않다
else: # 무게가 체력보다 작으면
    print("safe") # 안전하다
