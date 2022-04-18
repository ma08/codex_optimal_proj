
s = input()
t = input()

def count_correct_letters(s, t):
    correct = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            correct += 1
    return correct

print(count_correct_letters(s, t))
