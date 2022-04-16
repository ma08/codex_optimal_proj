# 파일에 쓰기

import sys

# 파일 객체 = open(파일 이름, 파일 열기 모드)

# r	읽기모드 - 파일을 읽기만 할 때 사용
# w	쓰기모드 - 파일에 내용을 쓸 때 사용
# a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("newFile.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
