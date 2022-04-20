# 문제
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
# 출력
# 두 번째로 큰 정수를 출력한다.

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a >= b:
    if a <= c:
        print(a)
    elif b >= c:
        print(b)
    else:
        print(c)
else:
    if a >= c:
        print(a)
    elif b <= c:
        print(b)
    else:
        print(c)
