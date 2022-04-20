
num_chars = int(input())
chars = input()

if num_chars % 2 == 1:
    print(0)
    print(chars)
else:
    num_deletions = num_chars
    for i in range(0, num_chars-1):
        if chars[i] != chars[i+1]:
            num_deletions -= 1
    print(num_deletions) 
    print(chars[0:num_deletions])
