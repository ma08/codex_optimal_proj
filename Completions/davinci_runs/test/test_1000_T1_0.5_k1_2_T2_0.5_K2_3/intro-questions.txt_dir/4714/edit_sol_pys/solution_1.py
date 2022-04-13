A, B = input().split()
A = int(A)
B = int(B)

def ispalindrome(num):
    num_str = str(num)
    ispalindrome = True
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[len(num_str) - i - 1]:
            ispalindrome = False
            break
    return ispalindrome


count = 0
for i in range(A, B + 1):
    if ispalindrome(i):
        count += 1

print(count)
