

num_chars = int(input())
chars = input()

if num_chars % 2 == 0:
    num_deletions = 0
    for i in range(0, num_chars-1, 2):
        if chars[i] == chars[i+1]:
            num_deletions += 1
    if num_deletions == 0:
        print(chars)
    else:
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0:
                print(chars[i:])
                break
            if chars[i] == chars[i+1]:
                num_deletions -= 1
            else:
                print(chars[i], end='')
else:
    num_deletions = 0
    for i in range(0, num_chars-2, 2):
        if chars[i] == chars[i+1]:
            num_deletions += 1
    print(num_deletions)
    print(num_deletions)
    if num_deletions == 0:
        print(chars)
    else:
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0:
                print(chars[i:])
                break
            if chars[i] == chars[i+1]:
                num_deletions -= 1
            else:
                print(chars[i], end='')
