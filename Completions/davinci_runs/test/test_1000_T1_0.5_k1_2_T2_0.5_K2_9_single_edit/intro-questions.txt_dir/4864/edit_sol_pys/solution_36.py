

r, c, zr, zc = map(int, input().split()) # r: 행의 개수, c: 열의 개수, zr: 행을 늘리는 배수, zc: 열을 늘리는 배수

article = [] # 입력 받은 문자열을 담을 배열
for i in range(r):
    article.append(input())

for i in range(r): # 행의 개수만큼 반복
    for j in range(zr): # zr만큼 반복
        for k in range(c): # 열의 개수만큼 반복
            for l in range(zc): # zc만큼 반복
                print(article[i][k], end="") # 입력 받은 문자열을 출력
        print() # 행 수를 늘려줌
