

def lcm(a,b):
    return a*b//gcd(a,b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)




num = int(input())

arr = list(map(int, input().split()))

for i in range(num):
    for j in range(i+1, num):
        if lcm(arr[i], arr[j]) == arr[i]*arr[j]:
            print('yes')
            exit()

print('no')
