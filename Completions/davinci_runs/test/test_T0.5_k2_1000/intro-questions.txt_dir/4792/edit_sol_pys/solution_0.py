

def remove_adjacent(nums):
    word = input()
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            word = word[:i] + word[i+1:]
            i -= 1

print(word)
