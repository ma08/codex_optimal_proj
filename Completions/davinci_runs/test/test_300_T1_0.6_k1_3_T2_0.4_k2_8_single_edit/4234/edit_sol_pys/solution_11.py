

num_chars = int(input(""))
chars = input("")

if num_chars % 2 == 1:
    print(num_chars, end="")
    print(chars, end="")
else:
    num_deletions = 0
    for i in range(0, num_chars-1, 2):
        if chars[i] == chars[i+1]:
            num_deletions += 1
    print(num_deletions, end="")
    if num_deletions == 0:
        print(chars, end="")
    else:
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0:
                print(chars[i:], end="")
                break
            if chars[i] == chars[i+1]:
                num_deletions -= 1
            else:
                print(chars[i], end='')
