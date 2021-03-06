

C, K = map(int, input().split()) # C와 K를 받아서 정수형으로 변환한다.

for i in range(K, 10): # K부터 10까지 반복한다.
    if C % (10**i) < 5*(10**(i-1)): # C를 10의 i승으로 나눈 나머지가 5*(10의 i-1승)보다 작으면
        C = C - C % (10**i) # C를 C를 10의 i승으로 나눈 나머지로 나눈다.
    else:
        C = C - C % (10**i) + 10**i # C를 C를 10의 i승으로 나눈 나머지로 나눈 뒤 10의 i승을 더한다.

print(C) # C를 출력한다.
