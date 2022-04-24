
n = int(input())
s = input()

for i in range(len(s)): # 0 ~ len(s)-1
    s = s[:i] + chr(ord(s[i]) + n) + s[i + 1:] # ord(s[i]) + n : 아스키코드 숫자로 바꾸고 n만큼 더하고 그걸 다시 아스키코드로 바꿔서 문자로 바꿔서 출력

print(s)
