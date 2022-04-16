

C, K = map(int, input().split()) # C: 정수, K: 자릿수
for i in range(K, 10): # 자릿수가 K부터 10까지
    if C % (10**i) < 5*(10**(i-1)): # 자릿수보다 작은 자리수의 수가 5보다 작으면
        C = C - C % (10**i) # 나머지를 빼준다.
    else:
        C = C - C % (10**i) + 10**i # 나머지를 빼고 10의 자릿수를 더해준다.

print(C)
