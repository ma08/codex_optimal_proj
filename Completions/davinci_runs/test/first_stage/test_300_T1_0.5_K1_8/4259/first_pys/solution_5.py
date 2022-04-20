

K = int(input())
A,B = map(int(input().split()))

if A % K == 0:
    print("OK")
elif B % K == 0:
    print("OK")
else:
    print("NG")