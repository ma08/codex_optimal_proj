

def check_palindrome(arr):
    if len(arr) < 3:
        return False
    for i in range(len(arr)):
        if i == 0:
            continue
        elif i == len(arr)-1:
            return True
        if arr[i] != arr[-i-1]:
            return False

def palindrome(arr):
    for i in range(len(arr)):
        for j in range(i+2, len(arr)+1):
            if check_palindrome(arr[i:j]):
                return True
    return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if palindrome(arr):
            print('YES')
        else:
            print('NO')