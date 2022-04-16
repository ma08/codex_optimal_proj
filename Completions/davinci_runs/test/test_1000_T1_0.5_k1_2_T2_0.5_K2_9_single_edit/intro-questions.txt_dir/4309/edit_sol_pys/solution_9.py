

# 파일 입출력

# 파일 읽기
# f = open("상대경로", "r")
# f = open("절대경로", "r")
# f = open("파일명", "r")
# f.read() # 파일 전체 읽기
# f.readline() # 한 줄 읽기
# f.readlines() # 여러 줄 읽기
# f.close()

# 파일 쓰기
# f = open("파일명", "w")
# f.write("텍스트")
# f.close()

# 예제1
f = open("newFile.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 예제2
f = open("newFile.txt", "r")
line = f.readline()
print(line)
f.close()

# 예제3
f = open("newFile.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 예제4
f = open("newFile.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 예제5
f = open("newFile.txt", "r")
data = f.read()
print(data)
f.close()

# with문과 함께 사용하기
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# sys 모듈로 입력 받기

import sys
N = int(sys.stdin.readline())

for i in range(100, N + 1):
    if len(set(list(str(i)))) == 1:
        print(i)
        break
