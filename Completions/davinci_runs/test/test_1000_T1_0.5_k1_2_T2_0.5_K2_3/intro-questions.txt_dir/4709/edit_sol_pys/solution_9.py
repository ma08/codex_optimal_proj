

# My Answer
a, op, b = input().split()
a = int(a)
b = int(b)

if op == '+':
    print(a + b)
else:
    print(a - b)

# eval() : 문자열로 인식된 수식을 계산해주는 함수
# Short Answer
a,op,b=input().split()
print(eval(a+op+b))


"""
-----Test Cases-----
Test Case 1
Input
1 + 2 
Output
3

Test Case 2
Input
1 - 2
Output
-1

Test Case 3
Input
100000 + 100000
Output
200000

Test Case 4
Input
100000 - 100000
Output
0
"""
