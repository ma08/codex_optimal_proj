
num_chars = int(input())
chars = input()

if num_chars % 2 == 1:
    print(num_chars)
    print(chars)
else:
    num_deletions = 0
    for i in range(0, num_chars - 1, 2):
        if chars[i] == chars[i+1]:
            num_deletions += 1
    print(num_deletions)
    if num_deletions == 0:
        print(chars)
    else:
        for i in range(0, num_chars - 1, 2):
            if num_deletions == 0:
                print(chars[i:])
                break
            if chars[i] == chars[i+1]:
                num_deletions -= 1
            else:
                print(chars[i], end='')
