

#import sys
#import io

#input_txt = """
#"""

#sys.stdin = io.StringIO(input_txt); sys.stdout = io.StringIO()
n,k,q = map(int, input().split())

arr_out = [0] * n
arr = [k] * n
for i in range(q):
    a = int(input())
    arr_out[a-1] += 1

for i in range(n):
    if arr[i] <= q - arr_out[i]:
        print("No")
    else:
        print("Yes")
