

A,B = input().split() # A:一つ目の文字列、B:二つ目の文字列
N = len(A)
M = len(B)

for i in range(M): # Bの文字列にあるAの文字列の一文字目を探す
    if B[i] in A: # Bの文字列にあるAの文字列の一文字目を探す
        break

print('.'*(N-1) + B[i]) # Bの文字列にあるAの文字列の一文字目を置き換えて出力
for j in range(M-1): # Bの文字列を置き換えて出力
    print('.'*(A.index(B[i])) + B[i] + '.'*(N-A.index(B[i])-1)) # Aの文字列を置き換えて出力
print(A) # Aの文字列を出力
for k in range(M-i-1): # Bの文字列にあるAの文字列の一文字目以外を置き換えて出力
    print('.'*N)
